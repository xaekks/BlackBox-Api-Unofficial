
import random
import strings
import requests
import cleverbotfreeapi
import json

from resources import anime, game

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"WELCOME TO NANDHA-API"}



@app.get("/neko", tags=['images'])
async def neko():
    url = random.choice(anime.neko)
    string = {"url": url}
    return string

@app.get("/chatbot/{prompt}", tags=['AI'])
async def chatbot(prompt):
     res = cleverbotfreeapi.cleverbot(prompt)
     respon = json.dumps({'text', res})
     response = json.loads(respon)
     return response 

@app.get("/ai/{model}/{prompt}", tags=['AI'])
async def ai_models(model, prompt):
     models = {
          'bard': 20,
          'gpt': 5,
          'palm': 1}
     
     names = list(models.keys())
     if model not in names:
           return "available model names: bard, gpt, palm"
     else:
         id = int(models[model])
         url = "https://lexica.qewertyy.dev/models?model_id={id}&prompt={prompt}"
         response = requests.post(url.format(id=id, prompt=prompt)).json()
         return response 



@app.get("/word", tags=['tools'])
async def ward():
     words_list = game.COMMON_WORDS
     random.shuffle(words_list)
     answer = random.choice(words_list)
     chars = list(word)
     random.shuffle(chars)
     question = '-'.join(chars)
     return {
        "question": question,
        "answer": answer 
     }

    
     
