=====
Usage
=====

To use person in a project::

    import person

Using Name::

    name = person.Name("Hans Hermann", "Bayer")
    print(name)

    Name:
    first_name=Hans
    last_name=Bayer
    middle_name_1=Hermann

Using Noble::

    noble = person.Noble("Dagmara", "Bodelschwingh", peer_title="Gräfin von")
    print(noble)

    Noble:
    first_name=Dagmara
    last_name=Bodelschwingh
    peer_preposition=von
    peer_title=Gräfin

Using Academic::

    academic = person.Academic("Horst Heiner", "Wiekeiner",
                               academic_title="Dr.")
    print(academic)

    Academic:
    academic_title=Dr.
    first_name=Horst
    last_name=Wiekeiner
    middle_name_1=Heiner

Using Person::

    person_1 = person.Person("Sven", "Rübennase", academic_title="MBA",
                             born="1990")
    print(person_1)

    Person:
    academic_title=MBA
    age=30
    born=1990
    first_name=Sven
    gender=male
    last_name=Rübennase

Using Politician::

    politician = person.Politician("Bärbel", "Gutherz", academic_title="Dr.",
                                   born="1980", party="SPD",
                                   electoral_ward="Köln I")
    print(politician)

    Politician:
    academic_title=Dr.
    age=40
    born=1980
    electoral_ward=Köln I
    first_name=Bärbel
    gender=female
    last_name=Gutherz
    parties=['SPD']
    party=SPD
    voter_count=121721
    ward_no=13

    politician.add_party("GRÜNE")
    politician.party='GRÜNE'
    politician.parties=['SPD', 'GRÜNE']

Using MdL::

    mdl = person.MdL("14", "Tom", "Schwadronius", peer_title="Junker von",
                     born="1950", party="Grüne")
    print(mdl)

    MdL:
    age=70
    born=1950
    first_name=Tom
    gender=male
    last_name=Schwadronius
    legislature=14
    parties=['Grüne']
    party=Grüne
    peer_preposition=von
    peer_title=Junker

    mdl.add_party("Grüne")
    mdl.change_ward("Düsseldorf II")
    print(mdl)

    MdL:
    age=70
    born=1950
    electoral_ward=Düsseldorf II
    first_name=Tom
    gender=male
    last_name=Schwadronius
    legislature=14
    parties=['SPD', 'Grüne']
    party=Grüne
    peer_preposition=von
    peer_title=Junker
    voter_count=99022
    ward_no=41
