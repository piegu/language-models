# Cursos | [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

[English](../en/README.md) | [Français](../fr/README.md) | **Português**

- **Crédito**: [DeepLearning.AI](https://www.deeplearning.ai) e [OpenAI](https://openai.com/)
- **Autor desta página**: [Pierre Guillou](https://www.linkedin.com/in/pierreguillou)
- **Data**: 6 de junho de 2023
- **Histórico**: Este curso originalmente criado para desenvolvedores ensina os princípios e as táticas a serem usadas para controlar o ChatGPT, ou seja, conduzi-lo através de uma instrução de linguagem natural para escrever um texto que atenda às suas expectativas. No entanto, como é basicamente aprender a falar com o ChatGPT e é possível fazê-lo sem qualquer código (ou seja, numa interface web), pareceu-me que todos poderiam beneficiar deste curso. Assim, decidi resumir cada um dos seus capítulos e listar os pontos-chave apresentados pelos formadores Isa Fulford (OpenAI) e Andrew Ng (DeepLearning.AI). Além dos falantes de inglês, decidi também facilitar seu acesso aos falantes de francês e português com versões traduzidas para seus respectivos idiomas.
- **Realização**: Então, como fazer tudo isso o mais rápido possível? Claro, trabalhei com um assistente... chamado ChatGPT 4. Usando minha conta pessoal no OpenAI, pedi ao ChatGPT para resumir as transcrições de texto de cada um dos vídeos do curso, para extrair os pontos principais do formulário de uma lista e, em seguida, traduza suas respostas textuais (as instruções usadas podem ser encontradas no apêndice). Fiz então uma revisão dos textos e possivelmente fiz algumas alterações quando julguei necessário (nada essencial). Finalmente, integrei todos os textos no github.
- **Nota**: As transcrições de texto e cadernos são disponibilizados por meio de links para permitir que todos possam obter as informações nesta página e facilitar sua implementação. No entanto, você deve se registrar na página do curso para assistir aos vídeos.

## Resumo

- [Lição 1 - Introdução](#lição-1---introdução)
- [Lição 2 - Princípios e táticas](#lição-2---princípios-e-táticas)
- [Lição 3 - Instrução interativa](#lição-3---instrução-interativa)
- [Lição 4 - Resumo e extração de informações](#lição-4---resumo-e-extração-de-informações)
- [Lição 5 - Inferência (classificação, detecção de tópicos, extração de informações)](#lição-5---inferência-classificação-topic-detection-information-extraction)
- [Lição 6 - Transformações](#lição-6---transformações)
- [Lição 7 - Assistente](#lição-7---assistente)
- [Lição 8 - ChatBot](#lesson-8---chatbot)
- [Lição 9 - Conclusão](#lição-9---conclusão)

## Lição 1 - Introdução

<img src="../images/lesson1/DeepLearning_course_ChatGPT_video1.png" width="400">

- **Recurso**: [transcrição 1](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video1.txt)

- **Resumo**: Este curso oferece um guia abrangente de instruções de engenharia do ChatGPT para desenvolvedores. Abrange as práticas recomendadas para o desenvolvimento de software usando modelos de linguagem grande (LLMs), incluindo o uso de chamadas de API para criar aplicativos. Ele diferencia entre LLMs principais e LLMs instrucionais, destacando os benefícios e aplicações destes últimos. O curso também ilustra a importância de instruções claras e específicas ao usar esses modelos.
- **Pontos chave**:
  - O curso é co-facilitado por Isa Fulford, membro da equipe da OpenAI, que tem experiência significativa com modelos linguísticos grandes (LLMs) e técnicas de prompt de ensino, e pelo professor de aprendizado profundo Andrew Ng, da Universidade de Stanford e criador do DeepLearning.AI.
  - Enfatiza o poder subestimado dos LLMs para que os desenvolvedores criem rapidamente aplicativos de software usando chamadas de API.
  - O programa cobrirá as melhores práticas para prompting (estratégia de declaração), casos de uso comuns (como resumir, inferir, transformar, expandir) e aplicações práticas como construir um chatbot usando um LLM.
  - O curso diferencia entre dois tipos de LLMs: LLMs básicos que prevêem a próxima palavra com base em dados de treinamento de texto e LLMs ajustados por instrução que seguem instruções específicas.
  - Os LLMs sintonizados com as instruções são preferidos devido à sua capacidade de seguir as instruções e aos seus recursos de segurança que os tornam menos propensos a produzir saídas tóxicas.
  - O curso enfatiza a importância de instruções claras e específicas para melhores resultados de um LLM concedido a instruções.
  - Vários colaboradores da OpenAI e DeepLearning.AI desempenharam um papel significativo na criação dos materiais do curso.

## Lição 2 - Princípios e Táticas

<img src="../images/lesson2/DeepLearning_course_ChatGPT_principles12.png" width="400">

- **Recursos**:
  - [transcrição 2](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video2.txt)
  - [l2-guidelines.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l2-guidelines.ipynb)

- **Resumo**: Neste curso, Isa discute diretrizes para sugestões eficazes com modelos de linguagem, com ênfase na clareza e especificidade das instruções e no tempo dado ao modelo para processar tarefas complexas. Além disso, apresenta táticas práticas, como o uso de delimitadores, solicitações de saída estruturada, verificação de instrução e aprendizado baseado em modelo a partir de alguns exemplos. As lições são ilustradas com exemplos de instruções envolvendo tarefas como resumir e traduzir textos, bem como resolver problemas matemáticos. A seção termina anunciando a próxima lição, que trata do processo de desenvolvimento iterativo da instrução.

- **Princípio 1**: **Escreva instruções claras e específicas**
  - **Objetivo**: Fornecer diretrizes explícitas e claras para orientar o modelo para a saída desejada e reduzir respostas irrelevantes ou incorretas. Aviso: instruções claras não significam curtas.
  - **Táticas**:
	1. **Uso de Delimitadores**: Marque claramente partes separadas da entrada com sinais de pontuação ou símbolos específicos para ajudar o modelo a entender melhor a instrução. Você pode usar os seguintes delimitadores, por exemplo: ```, """, < >, <tag> </tag>
	2. **Solicitar saída estruturada**: Isso pode facilitar a análise das saídas do modelo, solicitando saídas estruturadas como HTML ou JSON, ou até mesmo uma lista.
	3. **Verificação de condição**: instrua o modelo a verificar as suposições primeiro, ajudando a evitar erros e resultados inesperados. Peça uma saída diferente se a condição for verificada ou não.
	4. **Convide para se inspirar em alguns exemplos**: Forneça exemplos de execuções de tarefas bem-sucedidas para orientar a compreensão do modelo de tarefa necessário.

- **Princípio 2**: **Ajude o modelo a pensar**
  - **Objetivo**: Para tarefas complexas, ajudar o modelo a "pensar" pode evitar conclusões incorretas precipitadas. Isso envolve instruir o modelo a dedicar mais esforço computacional à tarefa.
  - **Táticas**:
	1. **Especificando etapas para tarefas**: detalhar as etapas para o modelo realizar uma tarefa pode melhorar seu desempenho e garantir que ele retorne o resultado desejado. O curso demonstrou isso com uma tarefa envolvendo resumir, traduzir, extrair nomes e produzir JSON (depois de listar as tarefas cronologicamente, informe ao modelo o formato de sua saída).
	2. **Peça ao modelo para encontrar suas próprias soluções**: O modelo de IA pode ser guiado para raciocinar soluções de forma independente antes de avaliar as soluções dos outros. O curso demonstrou isso com um problema de matemática, em que o modelo foi capaz de identificar um erro na solução de um aluno apenas quando solicitado a resolver o próprio problema primeiro.

**Limites do modelo**: **"Alucinações"**
- O curso alerta para um limite em que o modelo pode gerar respostas plausíveis, mas fabricadas, conhecidas como "alucinações". Foi mostrado um exemplo em que o modelo foi solicitado a descrever um modelo de escova de dentes inexistente e deu uma descrição realista, mas inventada.
- Para minimizar as alucinações, o modelo pode ser solicitado a encontrar citações relevantes em um texto e usar essas citações para responder a perguntas. Essa abordagem pode ajudar a rastrear a resposta até o documento de origem, fornecendo uma resposta mais confiável.

## Lição 3 - Instrução interativa

<img src="../images/lesson3/DeepLearning_course_ChatGPT_video3.png" width="400">

- **Recursos**:
  - [transcrição 3](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video3.txt)
  - [l3-iterative-prompt-development.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l3-iterative-prompt-development.ipynb)

- **Resumo**: Andrew enfatiza a importância do desenvolvimento de instrução iterativa ao usar modelos de linguagem grandes. Não é crucial que uma instrução funcione perfeitamente na primeira vez. É a melhoria da formação baseada em resultados que é a chave do sucesso. Andrew usa o exemplo de geração de um resumo para uma folha de especificações de cadeira, refinando a declaração para atender a várias restrições, como comprimento, detalhes técnicos e formato do texto produzido pelo ChatGPT. A importância de testar instruções em conjuntos de dados maiores à medida que os aplicativos amadurecem também é enfatizada.

- **Pontos chave**:
  - Desenvolver instruções eficazes para grandes modelos de linguagem é um processo iterativo.
  - A instrução perfeita geralmente não é alcançada na primeira tentativa, mas melhora com o tempo com base nos requisitos da aplicação e nos resultados anteriores.
  - Foi dado um exemplo de como refinar uma instrução para gerar um resumo de uma folha de especificações de cadeira, ajustando fatores como contagem de palavras, inclusão de detalhes técnicos e formato de saída (aqui, HTML).
  - Observou-se que grandes modelos de linguagem às vezes podem ter problemas com instruções para contagens de palavras ou caracteres muito precisos, mas esse não é o caso do ChatGPT, que é bastante confiável nesse assunto.
  - À medida que os aplicativos se tornam mais maduros, pode ser benéfico avaliar e refinar as instruções em relação a conjuntos maiores de exemplos para garantir um desempenho consistente em vários casos de uso.
  - O processo de desenvolvimento da instrução é importante, se não mais, do que conhecer a instrução perfeita. Trata-se de ter um bom processo para desenvolver instruções eficazes para aplicações específicas.

## Lição 4 - Resumo e extração de informações

<img src="../images/lesson4/DeepLearning_course_ChatGPT_video4.png" width="400">

- **Recursos**:
  - [transcrição 4](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video4.txt)
  - [l4-summarizing.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l4-summarizing.ipynb)

- **Resumo**: Andrew discute a utilidade de grandes modelos de linguagem para resumir textos, especialmente resenhas em um site de comércio eletrônico. Ele demonstra como esses modelos podem gerar resumos ou extrair informações específicas relevantes para diferentes departamentos (como frete ou preços), facilitando um processo de revisão mais eficiente e focado. Um código também é introduzido para resumir efetivamente várias revisões, permitindo acesso rápido ao seu conteúdo.

- **Pontos chave**:
  - Grandes modelos de linguagem podem ser usados ​​para resumir grandes volumes de texto, permitindo a compreensão efetiva do conteúdo.
  - Resumo específico pode ser gerado de acordo com os requisitos de diferentes departamentos, como remessa ou preços, com instruções personalizadas.
  - Andrew introduziu o conceito de extrair informações específicas em vez de fornecer um resumo geral, o que pode ser mais apropriado para determinados departamentos.
  - Uma implementação prática de um código de resumo de múltiplas revisões foi mostrada, permitindo acesso rápido à essência de múltiplas revisões.
  - Modelos de linguagem grandes não apenas ajudam a resumir, mas também podem ajudar a fazer inferências de textos, como determinar sentimentos positivos ou negativos em análises de produtos, que serão discutidas na próxima sessão.

## Lição 5 - Inferência (classificação, detecção de tópicos, extração de informações)

<img src="../images/lesson5/DeepLearning_course_ChatGPT_video5.png" width="400">

- **Recursos**:
  - [transcrição 5](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video5.txt)
  - [l5-inferring.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l5-inferring.ipynb)

- **Resumo**: Andrew discute como modelos de linguagem grandes podem ser usados ​​para inferir várias informações de texto, como sentimentos, expressões de emoções ou para extrair detalhes ou marcas de produtos, detecção de assuntos e como eles podem lidar com várias tarefas simultaneamente usando uma instrução codificada. Ele explica ainda mais as aplicações desses modelos para análises de clientes, identificando recursos específicos em texto e aprendizado instantâneo para detecção de tópicos em artigos de notícias.

- **Pontos chave**:
  - Grandes modelos de linguagem podem executar várias tarefas inferenciais, como análise de sentimentos, extração de nomes e rótulos e compreensão do contexto usando instruções textuais simples.
  - Os modelos podem processar e fornecer análises em uma string de texto com mais eficiência e rapidez em comparação com o fluxo de trabalho tradicional de aprendizado de máquina que requer modelos separados para diferentes tarefas.
  - Usando instruções específicas, os modelos podem não apenas classificar o sentimento de uma avaliação, mas também identificar a lista de emoções expressas e avaliar se um cliente está particularmente chateado. Essas informações podem ser valiosas para organizações de suporte ao cliente.
  - A extração de informações é outra capacidade importante de modelos de linguagem grandes que podem ser usados ​​para extrair e resumir informações importantes, como produto e fabricante, de uma grande coleção de revisões.
  - Modelos de linguagem grandes também podem lidar com instruções multitarefa, extraindo vários campos de uma string de texto em uma única instrução, economizando tempo de processamento e recursos.
  - Esses modelos podem inferir tópicos de um grande pedaço de texto, o que os torna úteis para analisar e categorizar grandes corpos de texto, como artigos de notícias.
  - O treinamento Zero Shot permite que o modelo identifique quais tópicos de uma lista predefinida são abordados em um determinado texto sem nenhum dado de treinamento específico.
  - Grandes modelos de linguagem podem construir rapidamente vários sistemas para inferências de texto que anteriormente levariam um tempo considerável, mesmo para desenvolvedores experientes de aprendizado de máquina.

## Lição 6 - Transformações

<img src="../images/lesson6/DeepLearning_course_ChatGPT_video6.png" width="400">

- **Recursos**:
  - [transcrição 6](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video6.txt)
  - [l6-transforming.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l6-transforming.ipynb)

- **Resumo**: Isa apresenta vários recursos dos principais modelos de linguagem, especialmente GPT-4, incluindo tradução de texto, transformação de tom, correções de ortografia e gramática e conversões de formato. Ele mostra como usar o GPT-4 em tarefas de tradução em vários idiomas e níveis de formalidade, apresenta o conceito de transformação de tom na escrita e demonstra recursos de revisão. Além disso, mostra a conversão de dados de um formato (JSON) para outro (HTML).

- **Pontos chave**:
  - Modelos de linguagem grandes podem traduzir texto em vários idiomas, incluindo versões informais e formais.
  - Eles podem detectar o idioma de um determinado texto, útil em um ambiente multilíngue como uma empresa multinacional de comércio eletrônico.
  - Os modelos podem mudar o tom do texto escrito, como transformar gírias em linguagem comercial.
  - Eles podem converter dados entre diferentes formatos (por exemplo: JSON para HTML).
  - GPT-4 pode ajudar a revisar e corrigir erros de gramática e ortografia no texto.
  - O GPT-4 também pode ajudar a transformar o texto para se ajustar a certos estilos e formatos, como estilo APA e formato de remarcação.

## Lição 7 - Assistente

<img src="../images/lesson7/DeepLearning_course_ChatGPT_video7.png" width="400">

- **Recursos**:
  - [transcrição 7](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video7.txt)
  - [l7-expanding.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l7-expanding.ipynb)

- **Resumo**: Isa discute os vários usos de grandes modelos de linguagem, incluindo tradução entre diferentes idiomas e formatos, correção ortográfica e gramatical, mudança de tom e expansão de texto. Ela também descreve como melhorar as instruções do modelo para obter resultados mais precisos e como criar um assistente de atendimento ao cliente de IA para responder às avaliações dos clientes.

- **Pontos chave**:
  - Ótimos modelos de idiomas podem traduzir texto entre diferentes idiomas e formatos e podem ajudar na correção ortográfica e gramatical.
  - Com instruções adequadas, o modelo pode alterar o tom de um texto para atender diferentes públicos.
  - Modelos de linguagem podem ser usados ​​para transformar textos curtos em textos mais longos, úteis para gerar conteúdo mais detalhado a partir de prompts.
  - O modelo pode ser usado como um assistente de atendimento ao cliente de IA para gerar respostas personalizadas às avaliações dos clientes.
  - O parâmetro de temperatura pode ser usado para controlar o grau de exploração ou variabilidade nas respostas do modelo.
  - É importante iterar e ajustar as instruções para obter resultados mais precisos.
  - É crucial ser transparente quando a IA gera texto para os usuários, informando que o texto foi gerado por um modelo de linguagem.

## Lição 8 - ChatBot

<img src="../images/lesson8/DeepLearning_course_ChatGPT_role.png" width="400">

- **Recursos**:
  - [transcrição 8](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video8.txt)
  - [l8-chatbot.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l8-chatbot.ipynb)

- **Resumo**: Isa discute como usar um modelo de linguagem amplo para construir um chatbot personalizado. Ela explica o formato OpenAI ChatCompletions, a função das mensagens do sistema e do usuário e a importância de fornecer contexto ao modelo para gerar respostas precisas. Ela apresenta exemplos de uso do chatbot para diferentes tarefas, como gerar piadas de Shakespeare e coletar pedidos de pizza. A transcrição também cobre o processo de criação de uma interface de usuário e adição de mensagens ao contexto da conversa. Por fim, mostra como gerar um resumo JSON baseado em conversa para processamento posterior.

- **Pontos chave**:
  - Modelos de linguagem ampla podem ser usados ​​para criar chatbots personalizados para várias tarefas.
  - O formato de chat envolve o uso de uma lista de mensagens, incluindo mensagens do sistema e do usuário.
  - As mensagens do sistema ajudam a definir o comportamento e a personalidade do assistente sem que o usuário perceba.
  - Fornecer contexto é crucial para que o modelo gere respostas precisas.
  - Uma interface de usuário pode ser criada para interagir com o chatbot e coletar consultas do usuário.
  - As conversas podem ser estendidas adicionando mensagens ao contexto.
  - O modelo pode gerar resumos JSON com base na conversa para processamento posterior.
  - A personalização do comportamento e da personalidade do chatbot pode ser obtida modificando a mensagem do sistema.

## Lição 9 - Conclusão

<img src="../images/lesson9/DeepLearning_course_ChatGPT_conclusion.png" width="400">

- **Recursos**:
  - [transcrição 9](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video9.txt)

- **Resumo**: Isa e Andrew concluem esta breve lição sobre técnicas de formulação de consultas, que destaca dois princípios fundamentais: escrever instruções claras e específicas e dar ao modelo tempo para pensar. Eles destacam a importância do desenvolvimento de consultas iterativas e da exploração dos diferentes recursos de grandes modelos de linguagem, como síntese, inferência, transformação e expansão. Eles incentivam os alunos a explorar suas próprias ideias de projeto, começando com pequenos projetos e melhorando gradualmente suas habilidades. O uso responsável de ferramentas de IA é enfatizado e os criadores do curso expressam seu entusiasmo pelo potencial do campo. A transcrição termina com um agradecimento e um convite para compartilhar os projetos concluídos.

- **Pontos chave**:
  - Dois princípios-chave para formular consultas: instruções claras e tempo para o modelo pensar.
  - A importância do desenvolvimento de consultas iterativas para encontrar a abordagem certa para aplicações específicas.
  - Diferentes capacidades de grandes modelos de linguagem, como síntese, inferência, transformação e expansão.
  - Incentivo para explorar as próprias ideias de projetos, mesmo começando com projetos pequenos ou divertidos.
  - A empolgação e o potencial de crescimento de criar aplicativos com grandes modelos de linguagem.
  - A importância do uso responsável das ferramentas de IA, com foco no impacto positivo.
  - Convite à partilha e divulgação do curso bem como dos projetos realizados.
