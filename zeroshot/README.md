this is a coding excersise for arabot
packaged using poetry

zeroshot is the package name and all required dependencies are in the pyproject.toml file

it uses a zero-shot classifier that is found in the huggingface library
it takes text and a list of candidate labels, whichever the label that is more associated with the text gets returned with a confidence score 
both inputs and outputs are in json formats

to run you would need poetry to make a virtual enviroment and install the required packages

then open zeroshot with uvicorn to be able to do post requests, i used thunder to make the request but you can use any other extension you like
to open up uvicorn type in "uvicorn zeroshot:app" in your terminal, uvicorn is already specified with FastAPI in the .toml file

you can look at the schema at /doc if you're using uvicorn under userRequest or use the interactive api

model used for the classification is digitalepidemiologylab/covid-twitter-bert-v2-mnli found at: https://huggingface.co/digitalepidemiologylab/covid-twitter-bert-v2-mnli


aalhelali99@hotmail.com

