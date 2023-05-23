# Curso: [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
De DeepLearning.AI e OpenAI

**Observação**: página escrita por ChatGPT 4

## Lição 1 - Introdução
- **Resumo**: Este curso oferece um guia abrangente sobre engenharia de prompt do ChatGPT para desenvolvedores. Ele abrange as melhores práticas para o desenvolvimento de software usando Modelos de Linguagem de Grande escala (LLMs), incluindo o uso de chamadas de API para construção de aplicações. Ele diferencia os LLMs básicos dos LLMs ajustados à instrução, destacando os benefícios e aplicações destes últimos. O curso também ilustra a importância de instruções claras e específicas ao utilizar esses modelos.
- Pontos-chave:
  - O curso é co-ministrado por Isa Fulford, membro da equipe da OpenAI, que tem experiência significativa com Modelos de Linguagem de Grande escala (LLMs) e ensino de técnicas de prompt.
  - Ele enfatiza o poder subestimado dos LLMs para desenvolvedores para construir rapidamente aplicações de software usando chamadas de API.
  - O currículo cobrirá as melhores práticas para a sugestão de comandos, casos de uso comuns (como resumir, inferir, transformar, expandir) e aplicações práticas, como construir um chatbot usando um LLM.
  - O curso diferencia entre dois tipos de LLMs: LLMs básicos que preveem a próxima palavra com base em dados de treinamento de texto, e LLMs ajustados à instrução que seguem instruções específicas.
  - Os LLMs ajustados à instrução são preferidos devido à sua capacidade de seguir instruções e seus recursos de segurança que os tornam menos propensos a produzir saídas tóxicas.
  - O curso enfatiza a importância de instruções claras e específicas para melhores resultados de um LLM ajustado à instrução.
  - Vários colaboradores da OpenAI e DeepLearning.ai desempenharam um papel significativo na criação dos materiais do curso.
- [transcrito 1](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video1.txt)

## Lição 2 - Instruções
- **Resumo**: O curso fornece táticas detalhadas para aumentar o desempenho dos modelos de IA. Ele demonstra a definição de etapas explícitas para tarefas como resumir texto e tradução, o que aumenta a previsibilidade e facilita a análise de código. Além disso, ele incentiva o modelo a resolver problemas independentemente antes de avaliar outras soluções, conforme exemplificado em um problema matemático. Para mitigar as 'alucinações', o curso propõe referenciar citações específicas de um texto-fonte. Finalmente, o curso explora a padronização da estrutura de saída, sugerindo o próximo tópico de desenvolvimento de prompts iterativos.
  - **Resumo (primeira parte)**: Neste curso, Isa discute diretrizes para a eficácia dos prompts com modelos de linguagem, com ênfase na clareza e especificidade das instruções e permitindo que o modelo tenha tempo para processar tarefas complexas. Além disso, ela introduz táticas práticas como o uso de delimitadores, solicitações de saída estruturadas, verificação de instruções e prompts de poucos disparos. A última parte do curso ilustra a configuração com a biblioteca Python OpenAI e a chave API, junto com o uso do modelo GPT 3.5 Turbo para conclusões de bate-papo.
  - **Resumo (segunda parte)**: A segunda parte do curso se concentra em refinar a precisão das respostas dos modelos de IA. Ele discute táticas como especificar etapas para uma tarefa, instruir o modelo a descobrir suas próprias soluções antes de decidir se a solução de outra pessoa está correta, e estar atento a limitações como 'alucinações' ou fabricações. As lições são ilustradas através de exemplos de prompts envolvendo tarefas como resumir e traduzir textos, bem como resolver problemas matemáticos. A seção termina dando uma pista sobre a próxima parte, que trata do processo de desenvolvimento de prompts iterativos.
- **Pontos-chave**:
  - Definir etapas explícitas para tarefas: Tornar explícitas as etapas necessárias para concluir uma tarefa melhora a qualidade das respostas do modelo de IA. Esta tática aumenta a previsibilidade da saída do modelo e facilita sua análise com código.
  - Encorajar a resolução de problemas de forma independente: Incentivar o modelo a elaborar uma solução por conta própria antes de avaliar outras soluções leva a respostas mais precisas, como demonstrado no contexto de um problema matemático.
  - Padronizar a estrutura de saída: Padronizar o formato da saída do modelo de IA ajuda na análise do código e torna a saída mais previsível. Isso pode ser feito especificando a estrutura de saída na solicitação.
  - Mitigar as alucinações: Para reduzir a tendência do modelo a 'alucinar' ou inventar informações, é recomendável pedir ao modelo que encontre primeiramente citações relevantes em um texto-fonte e baseie suas respostas nessas citações. Isso permite rastrear a resposta até o documento-fonte.
  - Desenvolvimento iterativo do prompt: Este curso sugere uma abordagem iterativa para o desenvolvimento de prompts para modelos de IA, que é o assunto da próxima parte do curso.
  - **Pontos-chave (primeira parte)**:
    - Princípio 1: Escreva instruções claras e específicas - Fornecer diretrizes explícitas e claras para guiar o modelo para a saída desejada e reduzir respostas irrelevantes ou incorretas.
    - Táticas para instruções claras:
      - Uso de delimitadores: Indicar claramente as partes distintas da entrada com pontuação ou símbolos específicos para ajudar o modelo a entender melhor o prompt.
      - Solicitar uma saída estruturada: Isso pode facilitar a análise das saídas do modelo, solicitando saídas estruturadas como HTML ou JSON.
      - Verificação de condição: Instruir o modelo para verificar primeiro suposições, ajudando a evitar erros e resultados inesperados.
      - Prompt de poucos disparos: Fornecer exemplos de execuções de tarefas bem-sucedidas para orientar a compreensão do modelo da tarefa necessária.
    - Princípio 2: Deixe o modelo pensar - Para tarefas complexas, permitir que o modelo "pense" pode evitar conclusões precipitadas incorretas. Isso envolve instruir o modelo a dedicar mais esforço de computação à tarefa.
    - Configuração da biblioteca Python OpenAI e chave API: Os usuários são orientados sobre como configurar e usar a biblioteca Python OpenAI e como recuperar e usar a chave API OpenAI.
    - Uso do modelo GPT 3.5 Turbo: O curso detalha o uso do modelo GPT 3.5 Turbo para conclusões de bate-papo e também introduz a função auxiliar, getCompletion, para facilitar o processamento de prompts.
  - **Pontos-chave (segunda parte)**: 
    - Especificação das etapas para tarefas: Detalhar as etapas para o modelo realizar uma tarefa pode melhorar seu desempenho e garantir que ele retorne o resultado desejado. O curso demonstrou isso com uma tarefa envolvendo resumir, traduzir, extrair nomes e saída JSON.
    - Instruir o modelo a encontrar suas próprias soluções: O modelo de IA pode ser orientado a raciocinar soluções de forma independente antes de avaliar as soluções dos outros. O curso demonstrou isso com um problema de matemática, onde o modelo foi capaz de identificar um erro na solução de um aluno apenas quando foi solicitado a resolver o problema por si mesmo primeiro.
    - Padronização da estrutura de saída: Implementar uma estrutura de saída padronizada pode facilitar a análise da saída com o código, levando a resultados mais previsíveis.
    - Limitações do modelo - 'Alucinações': O curso alerta sobre uma limitação onde o modelo pode gerar respostas plausíveis, mas inventadas, conhecidas como 'alucinações'. Um exemplo foi mostrado onde o modelo foi solicitado a descrever um modelo inexistente de escova de dentes e forneceu uma descrição realista, mas inventada.
    - Redução das alucinações: Para minimizar as alucinações, o modelo pode ser solicitado a encontrar citações relevantes em um texto e usar essas citações para responder a perguntas. Esta abordagem pode ajudar a rastrear a resposta até o documento-fonte, fornecendo uma resposta mais confiável.
    - Processo de desenvolvimento iterativo do prompt: O curso conclui preparando os alunos para a próxima parte - o processo de desenvolvimento iterativo do prompt, que é projetado para refinar o prompt do modelo.
- [transcrição 2](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video2.txt)
- [l2-guidelines.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l2-guidelines.ipynb)

## Lição 3 - Interativo
- [transcript 3](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video3.txt)
- [l3-iterative-prompt-development.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l3-iterative-prompt-development.ipynb)

## Lição 4 - Resumir
- [transcrição 4](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video4.txt)
- [l4-summarizing.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l4-summarizing.ipynb)

## Lição 5 - Inferência
- [transcrição 5](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video5.txt)
- [l5-inferring.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l5-inferring.ipynb)

## Lição 6 - Transforme
- [transcrito 6](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video6.txt)
- [l6-transforming.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l6-transforming.ipynb)

## Lição 7 - Expandir
- [transcript 7](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video7.txt)
- [l7-expanding.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l7-expanding.ipynb)

## Lição 8 - Chatbot
- [transcrito 8](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video8.txt)
- [l8-chatbot.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l8-chatbot.ipynb)

## Lição 9 - Conclusão
- [transcrição 9](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video9.txt)
