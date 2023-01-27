from django.shortcuts import render
from .models import *


# Create your views here.

def bangla_to_english(string):
    ref = {
        "০": "0",
        "১": "1",
        "২": "2",
        "৩": "3",
        "৪": "4",
        "৫": "5",
        "৬": "6",
        "৭": "7",
        "৮": "8",
        "৯": "9"
    }
    eng = ""
    for ch in string:
        eng += ref[ch]
    return eng


def english_to_bangla(string):
    ref = {
        "0": "০",
        "1": "১",
        "2": "২",
        "3": "৩",
        "4": "৪",
        "5": "৫",
        "6": "৬",
        "7": "৭",
        "8": "৮",
        "9": "৯"
    }
    bng = ""
    for ch in string:
        bng += ref[ch]
    return bng


def index(request):
    domain = request.get_host()
    admin_url = "http://" + domain + '/admin'
    if request.method == 'POST':
        searchKey = request.POST['searchField']
        results = []
        results.append(Assessment.objects.filter(nid_number=searchKey).first())
        results.append(Assessment.objects.filter(holding_number=searchKey).first())
        results.append(Assessment.objects.filter(mobile_no=searchKey).first())
        results = [i for i in results if i is not None]
        context = {
            "admin_url": admin_url,
            "title": "সার্চ পেইজ",
            "searching": True,
        }
        if len(results):
            context['result_found'] = True
            result = results[0]
            taxes = Tax.objects.filter(person=result, porishodh_status=False)
            bokeya = 0
            for tax in taxes:
                bokeya += int(bangla_to_english(tax.barshik_kor))
            if bokeya>0:
                bokeya = english_to_bangla(str(bokeya))
            else:
                bokeya = "নাই"
            context['bokeya'] = bokeya
            context['barir_malik'] = result.barir_malik
            context['pita_sami_nam'] = result.pita_sami_nam
            context['holding_number'] = result.holding_number
            context['barshik_mullayon'] = result.barshik_mullayon
            context['barshik_kor'] = result.barshik_kor
        else:
            context['result_found'] = False
        return render(request, 'maguraunion/base.html', context=context)
    return render(request, 'maguraunion/base.html', context={
        "admin_url": admin_url,
        "title": "হোমপেজ",
        "searching": False
    })
