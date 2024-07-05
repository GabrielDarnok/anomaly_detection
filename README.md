# Descrição
- Este script monitora dados de tráfego de rede em busca de anomalias usando o algoritmo Isolation Forest. Ele busca dados de uma API do Zabbix, processa-os e identifica anomalias em tempo real. Quando uma anomalia é detectada, uma notificação é enviada por meio de um webhook. O script é executado por um período especificado (1 hora) e gera gráficos dos dados de tráfego destacando as anomalias detectadas.

# Requisitos
- Python 3.10.12.
- Bibliotecas Python: requests, Pandas, scikit-learn, matplotlib,datetime, time.

# Uso
1.Certifique-se de ter o Python instalado em sua máquina.

2.Instale as bibliotecas necessárias executando o seguinte comando:

- | pip install requests pandas scikit-learn matplotlib |

3.Crie/Edite o arquivo config.json com as informações necessárias e a url do webhook.

4.Execute o script principal main.py:

- | python main.py |

# Estrutura do Projeto
- main.py: Script principal que coordena a execução dos outros scripts.
- utils/bytes.py: Script para alterar para GB.
- utils/config.py: Arquivo de configuração com informações necessarias. Também é armazenado no json a URL para o WebHook.
- utils/env_notf.py: Script feito para envio de notifiicações para o Slack.

# Autores
Gabriel Henrique

# Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo LICENSE.md para detalhes.