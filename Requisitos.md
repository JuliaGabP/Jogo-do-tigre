# Requisitos funcionais
### Funcionalidades que o sistema deve oferecer
### Cadastro de usuário
  - Descrição: O sistema deve permitir que novos usuários se cadastrem fornecendo um nome de usuário e uma senha.
  - Detalhes: O nome de usuário deve ser único.
  - A senha deve ser armazenada de forma segura (hash e salt).
      
### Autenticação de Usuário
  - Descrição: O sistema deve permitir que usuários façam login com seu nome de usuário e senha.
  - Detalhes: O sistema deve manter o usuário autenticado durante a sessão.
  - O usuário deve ser capaz de fazer logout.

### Saldo Inicial
  - Descrição: Ao se cadastrar, o usuário deve receber um saldo inicial fictício de 1000 unidades de dinheiro.

### Jogo de Aposta (Simulação do Jogo do Tigrinho)
  - Descrição: O usuário deve ser capaz de apostar uma quantia do seu saldo em uma rodada do jogo.
  - Detalhes: A cada rodada, o saldo do usuário deve ser atualizado com base no resultado (ganho ou perda).
  - A lógica do jogo deve ser baseada em probabilidades simples (por exemplo, chance de dobrar o valor apostado ou perder tudo).
  - O sistema deve impedir que o usuário aposte mais do que o saldo disponível.

### Monitoramento e Armazenamento de Histórico
  - Descrição: O sistema deve armazenar o histórico de cada rodada jogada por um usuário.
  - Detalhes: Cada rodada deve registrar a quantia apostada e o resultado da rodada.
  - O saldo atual do usuário deve ser registrado a cada jogada.

### Visualização de Gráfico
  - Descrição: Quando o saldo do usuário chegar a zero, o sistema deve exibir um gráfico mostrando a variação do saldo ao longo das rodadas.
  - Detalhes: O gráfico deve plotar o saldo do usuário em cada rodada, mostrando claramente os ganhos e perdas.

### Reiniciar Jogo
  - Descrição: Após visualizar o gráfico, o usuário deve ter a opção de reiniciar o jogo com um saldo de 1000 unidades.
  - Detalhes: O histórico anterior deve ser resetado ou armazenado de forma que não interfira na nova rodada.
  - O usuário deve poder repetir esse ciclo quantas vezes desejar.

# Requisitos não funcionais 
### Relacionados à qualidade e performance do sistema
### Segurança
  - Descrição: O sistema deve proteger as credenciais do usuário e seus dados.
  - Detalhes: Utilizar hashing de senhas.
  - Prevenir ataques como SQL Injection.
  - Usar HTTPS para comunicação segura.

### Performance
  - Descrição: O sistema deve responder de forma rápida e eficiente às interações do usuário.
  - Detalhes: O carregamento das páginas deve ser rápido.
  - A geração e exibição dos gráficos devem ser feitas em tempo real.

### Usabilidade
  - Descrição: O sistema deve ser fácil de usar, com uma interface clara e intuitiva.
  - Detalhes: As páginas devem ser responsivas, adaptando-se a diferentes dispositivos.
  - Mensagens de erro e sucesso devem ser claras e informativas.

### Escalabilidade
  - Descrição: O sistema deve ser capaz de lidar com um número crescente de usuários e dados.
  - Detalhes: Uso de um banco de dados que possa escalar conforme necessário (como PostgreSQL ou MySQL em produção).
  - Possibilidade de otimização futura para maior volume de acessos simultâneos.

### Manutenção
  - Descrição: O sistema deve ser fácil de manter e atualizar.
  - Detalhes: O código deve ser modular e seguir boas práticas de desenvolvimento.
  - Documentação clara para facilitar futuras alterações ou expansões.

# Histórico de versôes
| Versão | Data       | Descrição                                                                                                                                                                       | Autor                                        |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 1.0    | 21/08/2024 | Criação dos requisitos                                                                                                   | [Julia Gabriela](https://github.com/JuliaGabP) |
