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

## Lesson 3 - Interative
- [transcript 3](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video3.txt)
- [l3-iterative-prompt-development.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l3-iterative-prompt-development.ipynb)

## Lesson 4 - Summarizing
- [transcript 4](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video4.txt)
- [l4-summarizing.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l4-summarizing.ipynb)

## Lesson 5 - Inferring
- [transcript 5](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video5.txt)
- [l5-inferring.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l5-inferring.ipynb)

## Lesson 6 - Transforming
- [transcript 6](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video6.txt)
- [l6-transforming.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l6-transforming.ipynb)

## Lesson 7 - Expanding
- [transcript 7](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video7.txt)
- [l7-expanding.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l7-expanding.ipynb)

## Lesson 8 - Chatbot
- [transcript 8](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video8.txt)
- [l8-chatbot.ipynb](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/notebooks/l8-chatbot.ipynb)

## Lesson 9 - Conclusion
- [transcript 9](https://github.com/piegu/language-models/edit/master/chatgpt/deeplearning_ai_chatgpt_prompt_engineering_course/transcripts/transcript_video9.txt)
