from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.POST['fulltext']
    fulltextSplit = fulltext.split()
    wordDictionary = {}
    for word in fulltextSplit:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    sortedList = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    context = {'fulltext': fulltext, 'count': len(fulltextSplit), 'sortedList': sortedList}
    return render(request, 'count.html', context)


def about(request):
    return render(request, 'about.html')
