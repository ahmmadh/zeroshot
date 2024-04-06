from transformers import AutoTokenizer, BertForSequenceClassification, pipeline
from .api import userRequest, userResponse
from fastapi import FastAPI, HTTPException

app = FastAPI()
# so from the transformers library from huggingface we get an tokenizer, the model that was required and a pipleline
# the piple line is used to make the zero shot classifier where we inject the model and the tokenizer

tokenizer = AutoTokenizer.from_pretrained("digitalepidemiologylab/covid-twitter-bert-v2-mnli")

model = BertForSequenceClassification.from_pretrained("digitalepidemiologylab/covid-twitter-bert-v2-mnli")

# bert model COVID-Twitter-BERT v2 MNLI 


classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)



# here is the user's end code, we basically ask him for the text and the canditate labels, until he doesn't need to give out a label

# here we created a classify endpoint that takes a request, this request will hold the text and the candidate labels
@app.post("/classify", response_model=userResponse)
def classify(request: userRequest):
    
    text = request.text
    candidate_labels = request.canditate_labels

    res = classifier(text,candidate_labels)

# returning the label that we get from the classifier and the score through a response

    llabel = res['labels'][0]
    sscore = "%"+str(100*res['scores'][0])

    return userResponse(label=llabel,score=sscore)


#used thunder to send a post request containing text and label(s) to get the score