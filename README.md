# Reunion Automation
### Automação de Redatores e Oradores de uma Reunião

Este é um programa simples em Python que ajuda na seleção aleatória de um orador e um redator para uma reunião, mantendo o controle de participantes que estão ausentes ou que já foram escolhidos anteriormente.

## Funcionalidades

- **Leitura de Nomes:** O programa lê os nomes dos participantes de um arquivo de texto (`Nomes.txt`).
- **Seleção Aleatória:** Escolhe aleatoriamente um orador e um redator entre os participantes disponíveis.
- **Gestão de Ausências e Histórico:** Permite que você informe participantes ausentes e também registra os nomes escolhidos em reuniões anteriores para evitar seleções repetidas.
- **Persistência de Dados:** Mantém o histórico dos últimos nomes selecionados em um arquivo (`Last_reunion.txt`).

## Como Usar

1. **Configuração Inicial:**
   - Adicione os nomes dos participantes ao arquivo `Nomes.txt`, um por linha.

2. **Execução do Programa:**
   - Execute o script `main.py`.
   - Você será solicitado a fornecer os nomes dos participantes ausentes, se houver.
   - O programa selecionará automaticamente um orador e um redator entre os participantes disponíveis e exibirá os resultados.

3. **Atualização do Histórico:**
   - Após cada execução, o programa atualiza o arquivo `Last_reunion.txt` com os nomes escolhidos para evitar que sejam selecionados novamente na próxima reunião.

## Requisitos

- Python 3.x instalado no sistema.

## Arquivos Incluídos

- `main.py`: O script principal que executa a lógica de seleção de orador e redator.
- `Nomes.txt`: Arquivo onde são listados os nomes dos participantes.
- `Last_reunion.txt`: Arquivo que registra os últimos nomes selecionados para orador e redator.

## Notas Adicionais

- Certifique-se de que o arquivo `Nomes.txt` esteja atualizado com os participantes atuais antes de cada reunião.
- Caso ocorra um erro ou seja necessário modificar o comportamento do programa, revise e ajuste o código conforme necessário.
