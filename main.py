import requests
import json
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time
from utils.env_notf import formatMessage
from utils.config import webhook, url, headers, params
from utils.bytes import bytes_to_gb

anomalies_notf = set()
count = 0
last_notified_anomaly = None
last_notification_time = None

runtime = datetime.now() + timedelta(hours=1)

while datetime.now() < runtime:
    try:
        response = requests.post(url, headers=headers, data=json.dumps(params))
        traffic_data = response.json()['result']
        df = pd.DataFrame(traffic_data)

        df['clock'] = pd.to_datetime(df['clock'], unit='s')
        df['value'] = pd.to_numeric(df['value'])
        
        df['value_gb'] = df['value'].apply(bytes_to_gb)

        df.set_index('clock', inplace=True)

        intervalo = timedelta(minutes=15)
        tempo_atual = datetime.now()
        limite_inferior = tempo_atual - intervalo

        df_recente = df[df.index >= limite_inferior]

        model = IsolationForest(contamination=0.03, n_estimators=200, max_samples='auto', random_state=42)
        df_recente['anomaly'] = model.fit_predict(df_recente[['value_gb']])

        anomalies = df_recente[df_recente['anomaly'] == -1]
        
        if anomalies.index.max() != last_notified_anomaly:
            if last_notification_time is None or time.time() - last_notification_time >= 180:
                print("New anomaly detected:")
                print(anomalies)
                last_notification_time = time.time()
                formatMessage(webhook, "Anomaly identify")
            else:
                print("Cooldown active.")

        plt.figure(figsize=(10, 6))
        plt.plot(df_recente.index, df_recente['value_gb'], label='Tráfego (GB)')
        plt.scatter(anomalies.index, anomalies['value_gb'], color='red', label='Anomalia')
        plt.xlabel('Data')
        plt.ylabel('Tráfego (GB)')
        plt.legend()
        count+= 1
        plt.savefig(f'graph/anomaly_plot{count}.png')
            
        last_notified_anomaly = anomalies.index.max()

        plt.close()

    except requests.exceptions.RequestException as e:
        print(f"Error in the request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error when decoding JSON: {e}")

    time.sleep(60)

print("Completed script.")
