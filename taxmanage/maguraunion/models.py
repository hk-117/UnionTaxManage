from django.db import models
from . import commons


class Assessment(models.Model):
    barir_malik = models.CharField(max_length=64, verbose_name="বাড়ির মালিক")
    pita_sami_nam = models.CharField(max_length=64, verbose_name="পিতা/স্বামীর নাম")
    nid_number = models.CharField(max_length=20, verbose_name="এনআইডি নাম্বার")
    holding_number = models.CharField(max_length=32, verbose_name="হোল্ডিং নাম্বার")
    mobile_no = models.CharField(max_length=32, verbose_name="মোবাইল নাম্বার")
    ward_number = models.CharField(max_length=5, verbose_name="ওয়ার্ড নং")
    gramer_nam = models.CharField(max_length=128, verbose_name="গ্রামের নাম")
    para_moholla = models.CharField(max_length=128, verbose_name="পাড়া/মহল্লা")
    purush_songkha = models.CharField(max_length=10, verbose_name="পুরুষ")
    mohila_songkha = models.CharField(max_length=10, verbose_name="মহিলা")
    mot = models.CharField(max_length=10, verbose_name="মোট")
    voter_songkha = models.CharField(max_length=10, verbose_name="ভোটার সংখ্যা")
    bosot_bari_type = models.CharField(max_length=64, verbose_name="বসত বাড়ির ধরণ", choices=commons.BOSOT_BARI_OPTIONS)
    vita_jomi_poriman = models.CharField(max_length=10, verbose_name="ভিটার পরিমাণ")
    abadi_jomi_poriman = models.CharField(max_length=10, verbose_name="আবাদি জমির পরিমাণ")
    jomi_in_shotangso = models.CharField(max_length=10, verbose_name="জমি (শতাংশ)")
    latrin = models.BooleanField(default=True, verbose_name="ল্যাট্রিন")
    nolkup = models.BooleanField(default=True, verbose_name="নলকূপ")
    main_ay_source = models.CharField(max_length=64, verbose_name="প্রধান আয়ের উৎস",
                                      choices=commons.INCOME_SOURCE_OPTIONS)
    varatia_songkha = models.CharField(max_length=10, verbose_name="ভাড়াটিয়া গৃহের সংখ্যা", blank=True, null=True)
    varatia_ay = models.CharField(max_length=32, verbose_name="ভাড়াটিয়া গৃহের আয়", blank=True, null=True)
    protibondhi = models.BooleanField(default=False, verbose_name="প্রতিবন্ধী")
    vikkhuk = models.BooleanField(default=False, verbose_name="ভিক্ষুক")
    economic_class = models.CharField(max_length=64, verbose_name="অর্থনৈতিক শ্রেনী",
                                      choices=commons.ECONOMIC_CLASS_OPTIONS)
    barshik_mullayon = models.CharField(max_length=64, verbose_name="বার্ষিক মূল্যায়ন")
    barshik_kor = models.CharField(max_length=64, verbose_name="বার্ষিক করের পরিমান")

    def __str__(self):
        return f"{self.barir_malik} {self.holding_number}"


class Tax(models.Model):
    person = models.ForeignKey(Assessment, on_delete=models.CASCADE, verbose_name="বাড়ির মালিক")
    ortho_bochor = models.CharField(max_length=32, verbose_name="অর্থবছর")
    porishodh_status = models.BooleanField(default=False, verbose_name="পরিশোধ হয়েছে?")
    somoy = models.DateTimeField(verbose_name="তারিখ", blank=True, null=True)
    barshik_kor = models.CharField(max_length=64, verbose_name="পরিমান")

    def __str__(self):
        return f"{self.person} {self.ortho_bochor}"
