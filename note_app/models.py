from django.db import models

# Create your models here.



    # this feels so wrong but... https://docs.djangoproject.com/en/1.8/ref/models/fields/


class BookName(models.Model):
    Genesis = 'gen'
    Exodus = 'exo'
    Leviticus = 'lev'
    Numbers = 'num'
    Deuteronomy = 'deu'
    Joshua = 'jos'
    Judges = 'jdg'
    Ruth = 'rut'
    First_Samuel = '1sa'
    Second_Samuel = '2sa'
    First_Kings = '1ki'
    Second_Kings = '2ki'
    First_Chronicles = '1ch'
    Second_Chronicles = '2ch'
    Ezra = 'ezr'
    Nehemiah = 'neh'
    Esther = 'est'
    Job = 'job'
    Psalms = 'psa'
    Proverbs = 'pro'
    Ecclesiastes = 'ecc'
    Song_of_Solomon = 'son'
    Isaiah = 'isa'
    Jeremiah = 'jer'
    Lamentations = 'lam'
    Ezekiel = 'eze'
    Daniel = 'dan'
    Hosea = 'hos'
    Joel = 'joe'
    Amos = 'amo'
    Obadiah = 'oba'
    Jonah = 'jon'
    Micah = 'mic'
    Nahum = 'nah'
    Habakkuk = 'hab'
    Zephaniah = 'zep'
    Haggai = 'hag'
    Zechariah = 'zec'
    Malachi = 'mal'
    # New Test
    Matthew = 'mat'
    Mark = 'mar'
    Luke = 'luk'
    John = 'joh'
    Acts = 'act'
    Romans = 'rom'
    First_Corinthians = '1co'
    Second_Corinthians = '2co'
    Galatians = 'gal'
    Ephesians = 'eph'
    Philippians = 'phi'
    Colossians = 'col'
    First_Thessalonians = '1th'
    Second_Thessalonians = '2th'
    First_Timothy = '1ti'
    Second_Timothy = '2ti'
    Titus = 'tit'
    Philemon = 'phl'
    Hebrews = 'heb'
    James = 'jam'
    First_Peter = '1pe'
    Second_Peter = '2pe'
    First_John = '1jo'
    Second_John = '2jo'
    Third_John = '3jo'
    Jude = 'jud'
    Revelation = 'rev'

    books_of_the_bible_choices = (
        (Genesis, 'Genesis'),
        (Exodus, 'Exodus'),
        (Leviticus, 'Leviticus'),
        (Numbers, 'Numbers'),
        (Deuteronomy, 'Deuteronomy'),
        (Joshua, 'Joshua'),
        (Judges, 'Judges'),
        (Ruth, 'Ruth'),
        (First_Samuel, '1 Samuel'),
        (Second_Samuel, '2 Samuel'),
        (First_Kings, '1 Kings'),
        (Second_Kings, '2 Kings'),
        (First_Chronicles, '1 Chronicles'),
        (Second_Chronicles, '2 Chronicles'),
        (Ezra, 'Ezra'),
        (Nehemiah, 'Nehemiah'),
        (Esther, 'Esther'),
        (Job, 'Job'),
        (Psalms, 'Psalms'),
        (Proverbs, 'Proverbs'),
        (Ecclesiastes, 'Ecclesiastes'),
        (Song_of_Solomon, 'Song of Solomon'),
        (Isaiah, 'Isaiah'),
        (Jeremiah, 'Jeremiah'),
        (Lamentations, 'Lamentations'),
        (Ezekiel, 'Ezekiel'),
        (Daniel, 'Daniel'),
        (Hosea, 'Hosea'),
        (Joel,  'Joel'),
        (Amos,  'Amos'),
        (Obadiah,  'Obadiah'),
        (Jonah,  'Jonah'),
        (Micah,  'Micah'),
        (Nahum,  'Nahum'),
        (Habakkuk,  'Habakkuk'),
        (Zephaniah,  'Zephaniah'),
        (Haggai,  'Haggai'),
        (Zechariah,  'Zechariah'),
        (Malachi,  'Malachi'),
        # New Test
        (Matthew,  'Matthew'),
        (Mark,  'Mark'),
        (Luke,  'Luke'),
        (John,  'John'),
        (Acts,  'Acts'),
        (Romans,  'Romans'),
        (First_Corinthians,  '1 Corinthians'),
        (Second_Corinthians,  '2 Corinthians'),
        (Galatians,  'Galatians'),
        (Ephesians,  'Ephesians'),
        (Philippians,  'Philippians'),
        (Colossians,  'Colossians'),
        (First_Thessalonians,  '1 Thessalonians'),
        (Second_Thessalonians,  '2 Thessalonians'),
        (First_Timothy,  '1 Timothy'),
        (Second_Timothy,  '2 Timothy'),
        (Titus,  'Titus'),
        (Philemon,  'Philemon'),
        (Hebrews,  'Hebrews'),
        (James,  'James'),
        (First_Peter,  '1 Peter'),
        (Second_Peter,  '2 Peter'),
        (First_John,  '1 John'),
        (Second_John,  '2 John'),
        (Third_John,  '3 John'),
        (Jude,  'Jude'),
        (Revelation,  'Revelation'),
        )
    #models.CharField(max_length=3, choices=books_of_the_bible_choices, default=Genesis)
# class BookName(models.Model):
#     book_name_short = models.CharField(max_length=3)
#     book_name_long = models.CharField(max_length=)



class Anote(models.Model):
    book = models.CharField(max_length=10, choices=BookName.books_of_the_bible_choices, default=BookName.Genesis)
    #book = models.CharField(max_length=3,)
    chapter = models.IntegerField()
    verse = models.IntegerField(null=True)
    note_text = models.TextField(max_length=400)
    note_source = models.CharField(max_length=60, null=True)
    is_public = models.BooleanField(default=False)
    contributor = models.CharField(max_length=128)