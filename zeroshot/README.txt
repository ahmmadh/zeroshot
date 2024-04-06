this is a coding excersise for arabot
packaged using poetry

zeroshot is the package name and all required dependencies are in the pyproject.toml file

to run you would need poetry to make a virtual enviroment and install the required packages

then open zeroshot with uvicorn to be able to do post requests, i used thunder to make the request but you can use any other extension you like

you can look at the schema at /doc if you're using uvicorn under userRequest

model used for the classification is digitalepidemiologylab/covid-twitter-bert-v2-mnli found at: https://huggingface.co/digitalepidemiologylab/covid-twitter-bert-v2-mnli





