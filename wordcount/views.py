
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            #Increase
            word_dictionary[word] += 1
        else:
            #add to the worddictionary
            word_dictionary[word] = 1

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'word_dictionary':word_dictionary.items()})
