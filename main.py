# model's recovery 
import pickle

file = open('model1', 'rb')
model1 = pickle.load(file)
file.close()

file = open('model2', 'rb')
model2 = pickle.load(file)
file.close()


# API creation 

from fastapi import FastAPI, HTTPException

app = FastAPI()


import numpy as np 
from fastapi.responses import JSONResponse
import logging

@app.post("/prediction/Paris", description = 'nouvelle prediction')
async def prediction (longitude,latitude) : 
    """
    try : 
        p=model.predict([[longitude,latitude]]).tolist()
        result = {"prediction": prediction.item()} if isinstance(prediction, np.ndarray) else {"prediction": prediction}
        return JSONResponse(content=result)
    except Exception as e :
        raise HTTPException(status_code=500, detail="Internal Server Error", headers={"X-Error": str(e)})
    """
    return int(model1.predict([[longitude,latitude]]).tolist()[0])


@app.post("/predicctions/Ile_de_France", description = 'meilleur prediction, pour le vefa mettre 0 ou 1 pour oui ou non')
async def prediction (departement,n_pieces,vefa,surface_habitable,latitude, longitude) : 

    return int(model2.predict([[departement,n_pieces,vefa ,surface_habitable,latitude, longitude]]).tolist()[0])

        
    
