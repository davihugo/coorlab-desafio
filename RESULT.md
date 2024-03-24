# Resultado - Desafio CoorLab

# OBJETIVO DO PROJETO

O objetivo deste projeto era desenvolver uma aplicação web para calcular o valor de viagens de diferentes transportadoras com base no destino e data selecionados pelo usuário.

# Tecnologias Utilizadas

    - Vue.js para o frontend
    - Flask para o backend
    - BootstrapVue para estilização e componentes no frontend

# Arquitetura do Projeto

O projeto foi estruturado seguindo uma arquitetura de cliente-servidor. O frontend foi desenvolvido em Vue.js e o backend em Flask. A comunicação entre o frontend e o backend foi realizada por meio de requisições HTTP.

# Soluções Implementadas

    - Implementei uma API RESTful no backend Flask para lidar com as requisições do frontend.
    - Utilizei as bibliotecas Axios no frontend e Flask-CORS no backend para lidar com        problemas de CORS.

# Requisitos Funcionais:
    - Os usuários devem poder pesquisar viagens disponíveis com base no destino e na data desejados.
    - Os detalhes da viagem, como nome da transportadora, preço, duração e assento disponível, devem ser exibidos aos usuários.

# Requisitos não funcionais 
    - Desempenho:

    A aplicação deve ser responsiva e oferecer tempos de carregamento rápidos, garantindo uma experiência do usuário fluida.
    
    - Segurança:

    As informações dos usuários devem ser protegidas contra acesso não autorizado e vazamentos de dados.

    - Confiabilidade:

    A aplicação deve ser robusta e confiável, minimizando falhas e erros durante o uso normal.

    - Usabilidade:

    A interface do usuário deve ser intuitiva e fácil de usar, permitindo que os usuários naveguem facilmente pela aplicação e encontrem as informações desejadas.


# Melhorias Futuras

    Adicionar autenticação de usuários para garantir segurança e acesso restrito às funcionalidades.
    Implementar uma interface mais intuitiva e amigável para os usuários, incluindo a possibilidade de selecionar entre diferentes opções de viagem.
    Integrar um sistema de pagamento para permitir que os usuários realizem reservas de viagens diretamente pela aplicação.