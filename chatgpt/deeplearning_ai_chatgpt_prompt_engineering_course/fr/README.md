# Cours : [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
De DeepLearning.AI et OpenAI

**Note**: page écrite par ChatGPT 4.

## Leçon 1 - Introduction
- **Résumé**: Ce cours offre un guide complet sur l'ingénierie des invites ChatGPT pour les développeurs. Il couvre les meilleures pratiques pour le développement de logiciels utilisant les grands modèles linguistiques (LLMs), y compris l'utilisation d'appels API pour la construction d'applications. Il différencie les LLMs de base et les LLMs accordés aux instructions, mettant en évidence les avantages et les applications de ces derniers. Le cours illustre également l'importance des instructions claires et spécifiques lors de l'utilisation de ces modèles.
- **Points clés**: 
  - Le cours est co-animé par Isa Fulford, membre du personnel d'OpenAI, qui a une expérience significative avec les Grands Modèles Linguistiques (LLMs) et l'enseignement des techniques de prompt.
  - Il met l'accent sur le pouvoir sous-estimé des LLMs pour les développeurs pour construire rapidement des applications logicielles en utilisant des appels API.
  - Le programme couvrira les meilleures pratiques pour le prompting, des cas d'utilisation communs (tels que la résumé, l'inférence, la transformation, l'expansion) et des applications pratiques comme la construction d'un chatbot en utilisant un LLM.
  - Le cours fait la différence entre deux types de LLMs: les LLMs de base qui prédisent le mot suivant en fonction des données d'entraînement de texte, et les LLMs accordés aux instructions qui suivent des instructions spécifiques.
  - Les LLMs accordés aux instructions sont préférés en raison de leur capacité à suivre des instructions, et leurs caractéristiques de sécurité qui les rendent moins susceptibles de produire des sorties toxiques.
  - Le cours souligne l'importance d'instructions claires et spécifiques pour de meilleurs résultats d'un LLM accordé aux instructions.
  - Un certain nombre de contributeurs d'OpenAI et de DeepLearning.ai ont joué un rôle significatif dans la création des matériaux du cours.
- [transcription 1](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video1.txt)

## Leçon 2 - Consignes
- **Résumé**: Le cours fournit des tactiques détaillées pour augmenter les performances des modèles d'IA. Il démontre la définition d'étapes explicites pour des tâches comme la résumé de texte et la traduction, ce qui augmente la prévisibilité et facilite le traitement de code. De plus, il encourage le modèle à résoudre de manière autonome les problèmes avant d'évaluer d'autres solutions, comme exemplifié dans un problème mathématique. Pour atténuer les 'hallucinations', le cours propose de référencer des citations spécifiques d'un texte source. Enfin, le cours explore la standardisation de la structure de sortie, annonçant le prochain sujet du développement itératif d'invitations.
  - **Résumé (première partie)**: Dans ce cours, Isa discute des directives pour une invitation efficace avec les modèles de langage, avec un accent sur la clarté et la spécificité des instructions et le temps accordé au modèle pour traiter des tâches complexes. De plus, elle introduit des tactiques pratiques comme l'utilisation de délimiteurs, les demandes de sortie structurées, la vérification d'instructions, et l'invitation par quelques tirs. La dernière partie du cours illustre la configuration avec la bibliothèque Python OpenAI et la clé API, ainsi que l'utilisation du modèle GPT 3.5 Turbo pour les complétions de chat.
  - **Résumé (deuxième partie)**: La deuxième partie du cours se concentre sur l'affinement de la précision des réponses des modèles d'IA. Il discute de tactiques telles que la spécification des étapes pour une tâche, l'instruction du modèle pour trouver ses propres solutions avant de décider si la solution d'un autre est correcte, et la prise en compte de limitations comme les 'hallucinations' ou les fabrications. Les leçons sont illustrées par des exemples de prompts impliquant des tâches comme la résumé et la traduction de textes, ainsi que la résolution de problèmes mathématiques. La section se termine en annonçant la prochaine partie, traitant du processus de développement itératif de prompts.
- **Points clés**:
  - Définir des étapes explicites pour les tâches: Rendre explicites les étapes nécessaires pour accomplir une tâche améliore la qualité des réponses du modèle d'IA. Cette tactique augmente la prévisibilité de la production du modèle et facilite son analyse avec le code.
  - Encourager la résolution autonome de problèmes: Encourager le modèle à élaborer une solution de manière autonome avant d'évaluer d'autres solutions conduit à des réponses plus précises, comme illustré dans le contexte d'un problème de mathématiques.
  - Standardiser la structure de sortie: Standardiser le format de la sortie du modèle d'IA aide à l'analyse du code et rend la sortie plus prévisible. Cela peut être fait en spécifiant la structure de sortie dans l'invite.
  - Atténuer les hallucinations: Pour réduire la tendance du modèle à 'halluciner' ou à inventer des informations, il est recommandé de demander au modèle de trouver d'abord des citations pertinentes dans un texte source et de baser ses réponses sur ces citations. Cela permet de retracer la réponse au document source.
  - Développement itératif de l'invite: Ce cours suggère une approche itérative du développement d'invitations pour les modèles d'IA, qui est le sujet de la prochaine partie du cours.
  - **Points clés (première partie)**:
    - Principe 1: Rédiger des instructions claires et spécifiques - Fournir des directives explicites et claires pour guider le modèle vers la sortie souhaitée et réduire les réponses non pertinentes ou incorrectes.
    - Tactiques pour des instructions claires:
      - Utilisation de délimiteurs: Indiquer clairement les parties distinctes de l'entrée avec des signes de ponctuation ou des symboles spécifiques pour aider le modèle à mieux comprendre l'invite.
      - Demander une sortie structurée: Cela peut faciliter l'analyse des sorties du modèle, en demandant des sorties structurées comme HTML ou JSON.
      - Vérification de condition: Instruire le modèle pour vérifier d'abord les hypothèses, aidant à éviter les erreurs et les résultats inattendus.
      - Invitation à quelques tirs: Fournir des exemples de réussite d'exécutions de tâches pour guider la compréhension du modèle de la tâche requise.
    - Principe 2: Laisser le modèle réfléchir - Pour des tâches complexes, permettre au modèle de "réfléchir" peut éviter des conclusions incorrectes précipitées. Cela implique d'instruire le modèle pour qu'il consacre plus d'efforts de calcul à la tâche.
    - Configuration de la bibliothèque Python OpenAI et de la clé API: Les utilisateurs sont guidés sur la façon de configurer et d'utiliser la bibliothèque Python OpenAI et comment récupérer et utiliser la clé API OpenAI.
    - Utilisation du modèle GPT 3.5 Turbo: Le cours détaille l'utilisation du modèle GPT 3.5 Turbo pour les complétions de chat et introduit également la fonction d'aide, getCompletion, pour un traitement facile des invitations.
  - **Points clés (deuxième partie)**: 
    - Spécification des étapes pour les tâches: Détailler les étapes pour que le modèle puisse accomplir une tâche peut améliorer ses performances et garantir qu'il retourne le résultat souhaité. Le cours a démontré cela avec une tâche impliquant la résumé, la traduction, l'extraction de noms et la sortie JSON.
    - Instruire le modèle pour trouver ses propres solutions: Le modèle d'IA peut être guidé pour raisonner les solutions de manière indépendante avant d'évaluer les solutions des autres. Le cours a démontré cela avec un problème de mathématiques, où le modèle a pu identifier une erreur dans la solution d'un étudiant seulement lorsqu'il a été invité à résoudre le problème lui-même en premier.
    - Standardisation de la structure de sortie: Mettre en place une structure de sortie standardisée peut faciliter l'analyse de la sortie avec le code, conduisant à des résultats plus prévisibles.
    - Limitations du modèle - 'Hallucinations': Le cours met en garde contre une limitation où le modèle peut générer des réponses plausibles mais fabriquées, connues sous le nom de 'hallucinations'. Un exemple a été montré où le modèle a été invité à décrire un modèle de brosse à dents inexistant et a donné une description réaliste mais fabriquée.
    - Réduction des hallucinations: Pour minimiser les hallucinations, le modèle peut être invité à trouver des citations pertinentes dans un texte et utiliser ces citations pour répondre à des questions. Cette approche peut aider à retracer la réponse au document source, fournissant une réponse plus fiable.
    - Processus de développement itératif de l'invite: Le cours se conclut en préparant les apprenants pour la prochaine partie - le processus de développement itératif de l'invite, qui est conçu pour affiner l'invitation du modèle.
- [transcription 2](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video2.txt)
- [l2-guidelines.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l2-guidelines.ipynb)

## Leçon 3 - Interatif
- [transcription 3](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video3.txt)
- [l3-iterative-prompt-development.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l3-iterative-prompt-development.ipynb)

## Leçon 4 - Résumer
- [transcription 4](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video4.txt)
- [l4-summarizing.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l4-summarizing.ipynb)

## Leçon 5 - Inférence
- [transcription 5](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video5.txt)
- [l5-inferring.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l5-inferring.ipynb)

## Leçon 6 - Transformer
- [transcription 6](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video6.txt)
- [l6-transforming.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l6-transforming.ipynb)

## Leçon 7 - Développez
- [transcription 7](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video7.txt)
- [l7-expanding.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l7-expanding.ipynb)

## Leçon 8 - Chatbot
- [transcription 8](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video8.txt)
- [l8-chatbot.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l8-chatbot.ipynb)

## Leçon 9 - Conclusion
- [transcription 9](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video9.txt)
