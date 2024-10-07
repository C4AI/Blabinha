# Blabinha 2.0

Its second version (Blabinha 2.0) was implemented as an instance of a goal-oriented chat-like system. In this case, with interaction via chat (text), it uses OpenAI models and prompt engineering as the core of its reasoning. Since it is a goal-oriented system, it has some objectives to achieve during the conversation: introduction and contextualization of the dialogue; persuasion and engagement; scope restriction of interaction; use of appropriate language (for conversing with children); formulation of multiple-choice questions; and topic analysis. To learn more about Blabinha 2.0, you can access the conversation logs, the evaluation form used to evaluate it, and the results of this evaluation, all available in this directory.

## How to run

- **Inside the folder Versão 1.0** ->

- Create the .env file and insert the OpenAI api key:

        OPENAI_API_KEY="Insert the key here!"

- Create a the virtual environments:

        python -m venv ./venv

- Activate the venv(Windows example):

        \venv\Scripts\Activate.ps1

- Install all the requirements:

        pip install -r .\requirements.text

- Run the streamlit app:

        py -m streamlit run .\FrontPage.py

    Note that it will run the blue version. If you want to change to the red one insert in the addres "/FrontPageKomodo". It will be something like:

        http://localhost:8501/FrontPageKomodo