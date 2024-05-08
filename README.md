# Are LLMs good MT evaluators?

In this project we evaluate how three different state of the art decoder-only models are useful in regards to scoring machine translated sentence.

## 📝 Data

We evaluate 10 pairs of languages:

High resourced:
* English-Chinese (en-zh)
* English-Czech (en-cs)
* English-German (en-de)
* Finnish-English (fi-en)

Low resourced:
* German-French (de-fr)
* German-Czech (de-cs)
* Hindi-Bengali (hi-bn)
* Xhosa-Zulu (xh-zu)

## 💻 Models

We use three state-of-the-art decoder-only models via API calls:

* [Open-Mistral-7b](https://mistral.ai/news/announcing-mistral-7b/)
* [Gemma-7b-it](https://ai.google.dev/gemma/docs) 
* [Llama3-70b](https://llama.meta.com/llama3/)

## 🚀 Getting Started

Install all dependencies by doing:

```terminal
pip install -r requirements.txt
```

Set the environment variables by doing:

```terminal
touch .env
```

And fill this file with:
```
MISTRAL_API_KEY=<your_key>
GROQ_API_KEY=<your_key>
```
You are ready!
