from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class AssessmentCustom(admin.ModelAdmin):
    search_fields = ('=nid_number', '=holding_number', '=mobile_no')
    list_filter = ('ward_number', 'bosot_bari_type', 'main_ay_source', 'economic_class')
    list_display = (
        'barir_malik',
        'pita_sami_nam',
        'nid_number',
        'holding_number',
        'mobile_no',
        'ward_number',
        'gramer_nam',
        'para_moholla',
        'purush_songkha',
        'mohila_songkha',
        'voter_songkha',
        'bosot_bari_type',
        'vita_jomi_poriman',
        'abadi_jomi_poriman',
        'jomi_in_shotangso',
        'latrin',
        'nolkup',
        'main_ay_source',
        'varatia_songkha',
        'varatia_ay',
        'protibondhi',
        'vikkhuk',
        'economic_class',
        'barshik_mullayon',
        'barshik_kor',
    )
    fieldsets = [
        ("ব্যাক্তিগত তথ্য", {'fields': ['barir_malik', 'pita_sami_nam', 'nid_number', 'holding_number', 'mobile_no', 'ward_number', 'gramer_nam', 'para_moholla']}),
        ("পরিবারের সদস্য সংখ্যা", {"fields": ['purush_songkha', 'mohila_songkha', 'voter_songkha']}),
        ("সম্পদের বিবরণ", {'fields': ['bosot_bari_type', 'vita_jomi_poriman', 'abadi_jomi_poriman', 'jomi_in_shotangso', 'latrin', 'nolkup']}),
        ("আয়ের উৎস", {"fields": ['main_ay_source', 'varatia_songkha', 'varatia_ay']}),
        ("মূল্যায়ন", {"fields": ['protibondhi', 'vikkhuk', 'economic_class', 'barshik_mullayon', 'barshik_kor']})
    ]


class TaxCustom(admin.ModelAdmin):
    search_fields = ('=person__nid_number', '=person__holding_number', '=person__mobile_no')
    list_filter = ('person__ward_number', 'ortho_bochor', 'porishodh_status','somoy')
    list_display = (
        'person',
        'ortho_bochor',
        'porishodh_status',
        'somoy',
        'barshik_kor'
    )


admin.site.register(Assessment, AssessmentCustom)
admin.site.unregister(Group)
admin.site.register(Tax, TaxCustom)
