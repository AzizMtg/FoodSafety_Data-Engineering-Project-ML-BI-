from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm
from .models import Client
import joblib
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import logging
from owner.models import Facility

logger = logging.getLogger(__name__)

# Log sentiment prediction
logger.info(f"Comment: {Client.Comment} | Sentiment: {Client.Sentiment}")

def create_client(request, id):
    facility = get_object_or_404(Facility, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.facility = facility  # Associer la critique à l'installation
            # Perform sentiment analysis
            cleaned_comment = clean_comment(client.Comment)
            vectorized_comment = vectorizer.transform([cleaned_comment])
            prediction = svm_model.predict(vectorized_comment)[0]
            client.Sentiment = 'Satisfied' if prediction == 1 else 'Unsatisfied'

            client.save()
            return redirect('facility_detail', id=facility.id)  # Rediriger vers les détails de l'installation
    else:
        form = ClientForm()
    return render(request, 'client/create_review.html', {'facility': facility, 'form': form})

def clients_list(request):
    facilities = Facility.objects.all()
    return render(request, 'client/reviews_list.html', {'facilities': facilities})


def update_client(request, pk):
    client = Client.objects.get(id=pk)
    facility = client.facility  # Retrieve the associated facility from the client

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)

            # Re-run sentiment analysis on update
            cleaned_comment = clean_comment(client.Comment)
            vectorized_comment = vectorizer.transform([cleaned_comment])
            prediction = svm_model.predict(vectorized_comment)[0]
            client.Sentiment = 'Satisfied' if prediction == 1 else 'Unsatisfied'

            client.save()
            return redirect('facility_detail', id=facility.id)  # Redirect to facility details with its ID
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/update_review.html', {'form': form, 'client': client, 'facility': facility})

def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients_list')
    return render(request, 'client/delete_review.html', {'client': client})


# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load pre-trained model and vectorizer
from django.conf import settings

MODEL_PATH = settings.MODEL_PATH
import os
base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
svm_model_path = os.path.join(base_dir, '../py/svc_model.pkl')
vectorizer_path = os.path.join(base_dir, '../py/vectorizer.pkl')

svm_model = joblib.load(svm_model_path)
vectorizer = joblib.load(vectorizer_path)
# Stopwords for text cleaning
stop_words = set(stopwords.words('english'))

# Define negative words to retain
negative_words = {'not', 'never', 'no', 'none', 'nobody', 'nothing', 'neither', 'nowhere', 'hardly', 'scarcely', 'barely', 'without'}

# Remove negative words from stopwords
stop_words -= negative_words

# Function to clean comment text
def clean_comment(comment):
    comment = comment.lower()  # Convert to lowercase
    comment = re.sub(r'[^a-z\s]', '', comment)  # Remove special characters
    tokens = word_tokenize(comment)  # Tokenize the text
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]  # Remove stopwords (excluding negative words)
    return ' '.join(tokens)