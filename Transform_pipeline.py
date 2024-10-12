from transformers import pipeline
classifier = pipeline ("sentiment-analysis")
print (classifier("I definitevely love to make AI"))
