# Course: [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
From DeepLearning.AI and OpenAI 

## Lesson 1 - Introduction
- **Summary**: This course provides a comprehensive guide on ChatGPT prompt engineering for developers. It covers best practices for software development using Large Language Models (LLMs) including the use of API calls for application building. It differentiates between base LLMs and instruction-tuned LLMs, emphasizing the benefits and applications of the latter. The course also illustrates the importance of clear and specific instructions when utilizing these models.
- **Key Points**:
  - The course is co-taught by Isa Fulford, a staff member of OpenAI, who has significant experience with Large Language Models (LLMs) and teaching prompting techniques.
  - It emphasizes the underappreciated power of LLMs for developers to quickly build software applications using API calls.
  - The curriculum will cover best practices for prompting, common use cases (such as summarizing, inferring, transforming, expanding), and practical applications like building a chatbot using an LLM.
  - The course differentiates between two types of LLMs: base LLMs that predict the next word based on text training data, and instruction-tuned LLMs that follow specific instructions.
  - Instruction-tuned LLMs are preferred due to their ability to follow instructions, and their safety features which make them less likely to produce toxic outputs.
  - The course emphasizes the importance of clear and specific instructions for better results from an instruction-tuned LLM.
  - A number of contributors from OpenAI and DeepLearning.ai have played a significant role in the creation of the course materials.
- [transcript 1](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video1.txt)

## Lesson 2 - Guidelines

Principle 1 - Write clear and specific instructions.
Principle 2 - Give the model time to think.
 
Tactics for Principle 1:
- Use delimiters to clearly indicate distinct parts of the input.
- Ask for a structured output like HTML or JSON.
- Instruct the model to check whether conditions are satisfied.
- Use few-shot prompting and provide examples of successful executions of the task.

Tactics for Principle 2:
- Specify the steps required to complete a task.
- Instruct the model to work out its own solution before rushing to a conclusion.
- Ask the model to first find any relevant quotes from the text before generating answers to reduce hallucinations.


- **Summary**: The course provides detailed tactics to increase AI models' performance. It demonstrates defining explicit steps for tasks like text summarization and translation, which increases predictability and facilitates easier code parsing. Furthermore, it encourages the model to independently solve problems before evaluating other solutions, as exemplified in a mathematical problem. To mitigate 'hallucinations', the course proposes referencing specific quotations from a source text. Finally, the course explores output structure standardization, hinting at the next topic of iterative prompt development.
  - **Summary (first part)**: In this course, Isa discusses guidelines for effective prompting with language models, with an emphasis on clarity and specificity of instructions and allowing the model time to process complex tasks. Additionally, she introduces practical tactics such as the use of delimiters, structured output requests, instruction checking, and few-shot prompting. The latter part of the course illustrates setup with the OpenAI Python library and API key, along with the use of the GPT 3.5 Turbo model for chat completions.
  - **Summary (second part)**: The second part of the course focuses on refining AI models' response accuracy. It discusses tactics such as specifying steps for a task, instructing the model to figure out its own solutions before deciding if another's solution is correct, and being mindful of limitations like 'hallucinations' or fabrications. The lessons are illustrated through examples of prompts involving tasks like summarizing and translating texts, as well as solving mathematical problems. The section ends by hinting at the next part, dealing with the iterative prompt development process.
- **Key points**:
  - Define Explicit Steps for Tasks: Making the steps required to complete a task explicit improves the quality of AI model responses. This tactic increases the predictability of the model's output and makes it easier to parse with code.
  - Prompt for Independent Problem-Solving: Encouraging the model to independently work out a solution before assessing other solutions leads to more accurate responses, as illustrated in the context of a math problem.
  - Standardize Output Structure: Standardizing the format of the AI model's output helps with code parsing and makes the output more predictable. This can be done by specifying the output structure in the prompt.
  - Mitigate Hallucinations: To reduce the model's tendency to 'hallucinate' or make up information, it's recommended to ask the model to first find relevant quotes from a source text and base its responses on these quotes. This allows for traceability of the answer back to the source document.
  - Iterative Prompt Development: This course suggests an iterative approach to developing prompts for AI models, which is the topic of the next part of the course.
  - **Key points (first part)**:
    - Principle 1: Write clear and specific instructions - Provide explicit and clear directions to guide the model to the desired output and reduce irrelevant or incorrect responses.
    - Tactics for clear instructions:
      - Use of Delimiters: Clearly indicate distinct parts of the input with punctuation or specific symbols to help the model understand the prompt better.
      - Request Structured Output: This can facilitate parsing model outputs, by asking for structured outputs like HTML or JSON.
      - Condition Check: Instruct the model to verify assumptions first, helping avoid errors and unexpected results.
      - Few-shot Prompting: Provide examples of successful task executions to guide the model's understanding of the required task.
    - Principle 2: Give the model time to think - For complex tasks, allowing the model time to "think" can prevent rushed incorrect conclusions. This involves instructing the model to spend more computational effort on the task.
    - OpenAI Python library and API key setup: Users are guided on how to set up and use OpenAI's Python library and how to retrieve and use the OpenAI API key.
    - Usage of GPT 3.5 Turbo model: The course details using the GPT 3.5 Turbo model for chat completions and also introduces the helper function, getCompletion, for easy prompt processing.
  - **Key points (second part)**: 
    - Specifying Steps for Tasks: Detailing the steps for the model to complete a task can enhance its performance and ensure it returns the desired result. The course demonstrated this with a task involving summarization, translation, name extraction, and JSON output.
    - Instructing the Model to Figure Out Its Own Solutions: The AI model can be guided to reason out solutions independently before evaluating others' solutions. The course demonstrated this with a mathematical problem, where the model was able to identify an error in a student's solution only when prompted to solve the problem itself first.
    - Standardizing Output Structure: Implementing a standardized output structure can make it easier to parse the output with code, leading to more predictable results.
    - Model Limitations - 'Hallucinations': The course warns of a limitation where the model may generate plausible-sounding but fabricated responses, known as 'hallucinations'. An example was shown where the model was asked to describe a non-existent toothbrush model and gave a realistic-sounding but fabricated description.
    - Reducing Hallucinations: To minimize hallucinations, the model can be asked to find relevant quotes from a text and use those quotes to answer questions. This approach can help trace the answer back to the source document, providing a more reliable response.
    - Iterative Prompt Development Process: The course concludes by preparing learners for the next part - the iterative prompt development process, which is designed to fine-tune model prompting.
- [transcript 2](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video2.txt)
- [l2-guidelines.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l2-guidelines.ipynb)

## Lesson 3 - Interactive
- **Ressources**:
  - [transcript 3](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video3.txt)
  - [l3-iterative-prompt-development.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l3-iterative-prompt-development.ipynb)
- **Summary**: The speaker emphasizes the importance of iterative prompt development while working with large language models. It's not crucial for a prompt to work perfectly the first time, but instead refining the prompt based on outcomes is key to success. The speaker uses the example of generating a summary for a chair fact sheet, refining the prompt to meet different constraints like length, technical detail, and content format. The importance of testing prompts on larger data sets as applications mature is also highlighted.
- **Key points**: 
  - Developing effective prompts for large language models is an iterative process.
  - The perfect prompt isn't usually achieved on the first attempt, but rather it improves over time based on application's requirements and previous outcomes.
  - An example was given of refining a prompt to generate a summary of a chair fact sheet, adjusting for factors such as word count, inclusion of technical details, and output format (including HTML).
  - It was noted that large language models can sometimes struggle with instructions for very precise word counts or character counts, but they are generally reliable within reason.
  - As applications become more mature, it may be beneficial to evaluate and refine prompts against larger sets of examples to ensure consistent performance across various use cases.

## Lesson 4 - Summarizing
- **Ressources**: 
  - [transcript 4](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video4.txt)
  - [l4-summarizing.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l4-summarizing.ipynb)

- **Summary**: The speaker discusses the utility of large language models in summarizing text, particularly reviews on an e-commerce website. The speaker demonstrates how these models can generate summaries or extract specific information relevant to different departments (like shipping or pricing), thus facilitating a more efficient and targeted review process. A workflow is also introduced to efficiently summarize multiple reviews, allowing quick access to their content.

- **Key points**:
  - Large language models can be utilized to summarize large volumes of text, enabling efficient understanding of the content.
  - Specific summarization can be generated based on the requirements of different departments, e.g., shipping or pricing, through tailored prompts.
  - The speaker introduced the concept of extracting specific information rather than providing a general summary, which might be more suitable for certain departments.
  - A practical implementation of a review summarization workflow was shown, enabling quick access to the essence of multiple reviews.
  - Large language models not only help in summarizing but could also help in making inferences from text, such as determining positive or negative sentiment in product reviews, to be discussed in the next session.

## Lesson 5 - Inferring
- **Ressources**:
  - [transcript 5](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video5.txt)
  - [l5-inferring.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l5-inferring.ipynb)

- **Summary**: The transcript discusses how large language models can be used to infer various information from text such as sentiment, expressions of emotions, details about products or brands, topic detection, and how they can handle multiple tasks simultaneously with the help of prompts. It further elaborates on applications of such models for customer reviews, identifying specific features in a text, and zero-shot learning for topic detection in news articles.

- **Key points**:
  - Large language models can perform various inferential tasks like sentiment analysis, extracting names, labels, and understanding context by using simple text prompts.
  - The models can process and provide analysis on a text string in a more efficient and rapid manner compared to the traditional machine learning workflow that requires separate models for different tasks.
  - Using specific prompts, models can not only classify sentiment of a review but can also identify the list of emotions expressed and assess if a customer is particularly upset. This information can be valuable for customer support organizations.
  - Information extraction is another important capability of large language models which can be utilized to extract and summarize key information like the product and the manufacturer from a large collection of reviews.
  - Large language models can also handle multi-task prompts, extracting multiple fields out of a text string in a single prompt, saving processing time and resources.
  - These models can infer topics from a large piece of text, making it useful for analyzing and categorizing large bodies of text like news articles.
  - Zero-shot learning allows the model to identify which topics from a predefined list are covered in a given text without any specific training data.
  - Large language models can rapidly build multiple systems for text inferences which would have previously taken a considerable amount of time even for skilled machine learning developers.

## Lesson 6 - Transforming
- **Ressources**:
  - [transcript 6](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video6.txt)
  - [l6-transforming.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l6-transforming.ipynb)

- **Summary**: Isa presents several capabilities of large language models, specifically GPT-4, including text translation, tone transformation, spelling and grammar corrections, and format conversions. He demonstrates how to use GPT-4 in translation tasks across various languages and levels of formality, introduces the concept of tone transformation in writing, and demonstrates proofreading capabilities. Additionally, he demonstrates converting data from one format (JSON) to another (HTML).

- **Key points**:
  - Large language models can translate text across multiple languages, including informal and formal versions.
  - They can detect the language of a given text, useful in a multi-lingual environment like a multinational e-commerce company.
  - Models can alter the tone of the written text, such as transforming slang into business language.
  - They can convert data between different formats (example: JSON to HTML).
  - GPT-4 can help with proofreading and correcting grammar and spelling errors in the text.
  - GPT-4 can also help in transforming the text to fit certain styles and formats, such as APA style and markdown format.
  - Lastly, the speaker teases the next topic which is expanding shorter prompts to generate a longer, more freeform response from a language model.

## Lesson 7 - Expanding
- **Ressources**:
  - [transcript 7](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video7.txt)
  - [l7-expanding.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l7-expanding.ipynb)

- **Summary**: The teacher discusses applications of large language models like translation, tone transformation, format conversion, proofreading, and generating a personalized email response. The transcript provides several demonstrations, such as translating between languages, adjusting formal and informal language in translation, converting JSON to HTML, proofreading and correcting grammar and spelling errors, and crafting an email response based on customer review sentiment. It also discusses the concept of 'temperature' in language model responses.

- **Key points**:
  - Large language models can translate between different languages, correct grammar and spelling, and convert between formats like JSON and HTML.
  - Formal and informal tones can be adjusted in translation based on the relationship of the speaker and listener.
  - A language model can be used as a universal translator, capable of translating multiple languages into desired languages.
  - Language models can transform tone, such as changing text from slang to a business letter format.
  - Language models can proofread and correct text, checking grammar and spelling, and making text more compelling.
  - The concept of 'temperature' in language models allows control over the randomness of the model's responses.
  - Language models can generate personalized email responses based on input sentiment, maintaining transparency that the response was generated by AI.

## Lesson 8 - Chatbot
- [transcript 8](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video8.txt)
- [l8-chatbot.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l8-chatbot.ipynb)

## Lesson 9 - Conclusion
- [transcript 9](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video9.txt)
