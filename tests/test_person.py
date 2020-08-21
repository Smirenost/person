#!/usr/bin/env python
# test_person.py
"""Tests for `person` package."""
# pylint: disable=redefined-outer-name

from person import person
import pytest


names = [["Alfons-Reimund Horst Emil", "Boeselager"],
         ["Horatio R.", "Pimpernell"],
         ["Sven Jakob", "Große Brömer"]]


def equivalent_names(n1, n2):
    fn = n2[0].split()[0]
    ln = n2[-1]
    try:
        mn_2 = n2[0].split()[2]
    except IndexError:
        mn_2 = None
    try:
        mn_1 = n2[0].split()[1]
    except IndexError:
        mn_1 = None

    return ((n1.first_name == fn) and
            (n1.middle_name_1 == mn_1) and
            (n1.middle_name_2 == mn_2) and
            (n1.last_name == ln))


@pytest.mark.parametrize("n", names)
def test_person_Name_para(n):
    name = person.Name(*n)
    assert equivalent_names(name, n)


def test_person_Name(name_fixture):
    # pylint: disable=W0612, W0613

    name = person.Name("Alfons-Reimund Horst Emil", "Boeselager")
    assert name.first_name == "Alfons-Reimund"
    assert name.middle_name_1 == "Horst"
    assert name.middle_name_2 == "Emil"
    assert name.last_name == "Boeselager"


def test_person_Academic(academic_fixture):
    # pylint: disable=W0612, W0613

    academic = person.Academic(
        "Horatio", "Pimpernell", middle_name_1="R.", academic_title="Prof.Dr.   Dr"
    )
    assert academic.first_name == "Horatio"
    assert academic.middle_name_1 == "R."
    assert academic.last_name == "Pimpernell"
    assert academic.academic_title == "Prof. Dr. Dr."

    academic = person.Academic(
        "Horatio Rübennase D.", "Pimpernell", academic_title="Prof.Dr.Dr"
    )
    assert academic.first_name == "Horatio"
    assert academic.middle_name_1 == "Rübennase"
    assert academic.middle_name_2 == "D."
    assert academic.last_name == "Pimpernell"
    assert academic.academic_title == "Prof. Dr. Dr."

    academic = person.Academic("Horatio", "Pimpernell", academic_title="B.A.")
    assert academic.academic_title == "B. A."


def test_person_Noble(noble_fixture):
    # pylint: disable=W0612, W0613

    noble = person.Noble("Sepp Theo", "Müller", peer_title="von und zu")

    assert noble.first_name == "Sepp"
    assert noble.middle_name_1 == "Theo"
    assert noble.last_name == "Müller"
    assert noble.peer_preposition == "von und zu"

    noble = person.Noble("Seppl", "Müller", peer_title="Junker van")

    assert noble.first_name == "Seppl"
    assert noble.last_name == "Müller"
    assert noble.peer_title == "Junker"
    assert noble.peer_preposition == "van"

    noble = person.Noble("Sven Oskar", "Müller", peer_title="Graf Eumel von")

    assert noble.first_name == "Sven"
    assert noble.middle_name_1 == "Oskar"
    assert noble.last_name == "Müller"
    assert noble.peer_title == "Graf"
    assert noble.peer_preposition == "von"


def test_person_Person(person_fixture):
    # pylint: disable=W0612, W0613

    pers = person.Person("Hugo", "Berserker", academic_title="MBA", born="2000")

    assert pers.gender == "male"
    assert pers.academic_title == "MBA"
    assert pers.age == "20"

    pers = person.Person("Siggi Mathilde", "Berserker", born="1980-2010")

    assert pers.gender == "unknown"
    assert pers.middle_name_1 == "Mathilde"
    assert pers.born == "1980"
    assert pers.deceased == "2010"

    pers = person.Person("Sigrid", "Berserker")

    assert pers.gender == "female"


def test_person_Politician(politician_fixture):
    # pylint: disable=W0612, W0613

    pol_1 = person.Politician(
        "Regina",
        "Dinther",
        party="CDU",
        peer_title="van",
        electoral_ward="Rhein-Sieg-Kreis IV",
    )

    assert pol_1.first_name == "Regina"
    assert pol_1.last_name == "Dinther"
    assert pol_1.gender == "female"
    assert pol_1.peer_preposition == "van"
    assert pol_1.party == "CDU"
    assert pol_1.ward_no == 28
    assert pol_1.voter_count == 110389

    pol_1.party = "fraktionslos"
    assert pol_1.party == "fraktionslos"
    assert pol_1.parties == ["CDU"]

    pol_2 = person.Politician(
        "Regina",
        "Dinther",
        party="CDU",
        electoral_ward="Landesliste",
    )

    assert pol_2.electoral_ward == "ew"

    pol_3 = person.Politician(
        "Heiner", "Wiekeiner", electoral_ward="Kreis Aachen I"
    )

    assert pol_3.voter_count == 116389

    pol_5 = person.Politician("Heiner", "Wiekeiner", electoral_ward="Köln I")

    assert pol_5.ward_no == 13
    assert pol_5.voter_count == 121721


def test_person_MdL(mdl_fixture):
    # pylint: disable=W0612, W0613

    mdl = person.MdL(
        "14",
        "Alfons-Reimund",
        "Hubbeldubbel",
        party="Grüne",
        peer_title="auf der",
        electoral_ward="Ennepe-Ruhr-Kreis I",
        minister="JM",
    )
    mdl.party = "SPD"

    assert mdl.legislature == "14"
    assert mdl.first_name == "Alfons-Reimund"
    assert mdl.last_name == "Hubbeldubbel"
    assert mdl.gender == "male"
    assert mdl.peer_preposition == "auf der"
    assert mdl.party == "SPD"
    assert mdl.parties == ["Grüne"]
    assert mdl.ward_no == 105
    assert mdl.minister == "JM"


def test_person_TooManyFirstNames(toomanyfirstnames_fixture):
    # pylint: disable=W0612, W0613

    from person.person import TooManyFirstNames

    name = person.Name
    with pytest.raises(TooManyFirstNames):
        name("Alfons-Reimund Horst Emil Pupsi", "Schulze")


def test_person_NotInRangeError(notinrange_fixture):
    # pylint: disable=W0612, W0613

    from person.person import NotInRange

    mdl = person.MdL

    with pytest.raises(NotInRange):
        mdl("100", "Alfons-Reimund", "Hubbeldubbel")


def test_person_AttrDisplay(capsys, attrdisplay_fixture):
    # pylint: disable=W0612, W0613

    from person.person import AttrDisplay
    from dataclasses import dataclass

    @dataclass
    class MockClass(AttrDisplay):
        a: str
        b: str
        c: str

    attr_1 = "späm"
    attr_2 = "ham"
    attr_3 = "ew"

    mock_instance = MockClass(attr_1, attr_2, attr_3)
    print(mock_instance)
    captured = capsys.readouterr()

    expected = """MockClass:\na=späm\nb=ham\n\n"""

    assert expected == captured.out
