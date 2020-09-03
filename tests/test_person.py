#!/usr/bin/env python
# test_person.py
"""Tests for `person` package."""
# pylint: disable=redefined-outer-name

import pytest

from person import person
from person.person import NotGermanParty, Party

names = [
    ["Alfons-Reimund Horst Emil", "Boeselager"],
    ["Horatio R.", "Pimpernell"],
    ["Sven Jakob", "Große Brömer"],
]


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

    return (
        (n1.first_name == fn)
        and (n1.middle_name_1 == mn_1)
        and (n1.middle_name_2 == mn_2)
        and (n1.last_name == ln)
    )


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
        "Horatio",
        "Pimpernell",
        middle_name_1="R.",
        academic_title="Prof.Dr.   Dr",  # noqa
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

    pers = person.Person("Hugo", "Berserker", academic_title="MBA", born="2000")  # noqa

    assert pers.gender == "male"
    assert pers.academic_title == "MBA"
    assert pers.age == "20"

    pers = person.Person("Siggi Mathilde", "Berserker", born="1980-2010")

    assert pers.gender == "unknown"
    assert pers.middle_name_1 == "Mathilde"
    assert pers.born == "1980"
    assert pers.deceased == "2010"

    pers = person.Person("Sigrid", "Berserker", date_of_birth="10.1.1979")  # noqa

    assert pers.gender == "female"
    assert pers.born == "1979"


def test_person_Politician(politician_fixture):
    # pylint: disable=W0612, W0613

    pol_1 = person.Politician(
        "CDU",
        "Regina",
        "Dinther",
        peer_title="van",
        electoral_ward="Rhein-Sieg-Kreis IV",
    )

    assert pol_1.first_name == "Regina"
    assert pol_1.last_name == "Dinther"
    assert pol_1.gender == "female"
    assert pol_1.peer_preposition == "van"
    assert pol_1.party_name == "CDU"
    assert pol_1.ward_no == 28
    assert pol_1.voter_count == 110389

    pol_1.party_name = "fraktionslos"
    assert pol_1.party_name == "fraktionslos"
    assert pol_1.parties == [
        Party(party_name="CDU", party_entry="unknown", party_exit="unknown")
    ]  # noqa

    pol_2 = person.Politician(
        "CDU", "Regina", "Dinther", electoral_ward="Landesliste",
    )  # noqa

    assert pol_2.electoral_ward == "ew"

    pol_3 = person.Politician(
        "Piraten", "Heiner", "Wiekeiner", electoral_ward="Kreis Aachen I"
    )  # noqa

    assert pol_3.voter_count == 116389

    with pytest.raises(NotGermanParty):
        pol_4 = person.Politician("not_a_German_party", "Thomas", "Gschwindner")  # noqa

    pol_4 = person.Politician("FDP", "Thomas", "Gschwindner")
    pol_4.add_Party("FDP")

    assert pol_4.party_name == "FDP"
    assert pol_4.parties == [
        Party(party_name="FDP", party_entry="unknown", party_exit="unknown")
    ]  # noqa

    pol_4.add_Party("not_a_German_party")

    assert pol_4.party_name == "FDP"
    assert pol_4.parties == [
        Party(party_name="FDP", party_entry="unknown", party_exit="unknown")
    ]  # noqa

    pol_4.add_Party("AfD")

    assert pol_4.parties == [
        Party(party_name="FDP", party_entry="unknown", party_exit="unknown"),
        Party(party_name="AfD", party_entry="unknown", party_exit="unknown"),
    ]

    pol_4.add_Party("AfD", party_entry="2019")

    assert pol_4.party_entry == "2019"
    assert pol_4.parties == [
        Party(party_name="FDP", party_entry="unknown", party_exit="unknown"),
        Party(party_name="AfD", party_entry="2019", party_exit="unknown"),
    ]

    pol_4.add_Party("AfD", party_entry="2019", party_exit="2020")

    assert pol_4.party_exit == "2020"
    assert pol_4.parties == [
        Party(party_name="FDP", party_entry="unknown", party_exit="unknown"),
        Party(party_name="AfD", party_entry="2019", party_exit="2020"),
    ]

    pol_5 = person.Politician(
        "Linke", "Heiner", "Wiekeiner", electoral_ward="Köln I"
    )  # noqa

    assert pol_5.ward_no == 13
    assert pol_5.voter_count == 121721

    pol_6 = person.Politician("Grüne", "Heiner", "Wiekeiner")

    assert pol_6.electoral_ward == "ew"
    assert pol_6.ward_no is None
    assert pol_6.voter_count is None

    pol_6.change_ward("Essen III")

    assert pol_6.electoral_ward == "Essen III"
    assert pol_6.ward_no == 67
    assert pol_6.voter_count == 104181


def test_person_MdL(mdl_fixture):
    # pylint: disable=W0612, W0613

    mdl = person.MdL(
        "14",
        "NRW",
        "Grüne",
        "Alfons-Reimund",
        "Hubbeldubbel",
        peer_title="auf der",
        electoral_ward="Ennepe-Ruhr-Kreis I",
        minister="JM",
    )

    assert mdl.legislature == "14"
    assert mdl.first_name == "Alfons-Reimund"
    assert mdl.last_name == "Hubbeldubbel"
    assert mdl.gender == "male"
    assert mdl.peer_preposition == "auf der"
    assert mdl.party_name == "Grüne"
    assert mdl.parties == [
        Party(party_name="Grüne", party_entry="unknown", party_exit="unknown")
    ]  # noqa
    assert mdl.ward_no == 105
    assert mdl.minister == "JM"

    mdl.add_Party("fraktionslos")
    assert mdl.party_name == "fraktionslos"
    assert mdl.parties == [
        Party(party_name="Grüne", party_entry="unknown", party_exit="unknown"),
        Party(
            party_name="fraktionslos",
            party_entry="unknown",
            party_exit="unknown",  # noqa
        ),
    ]


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
        mdl("100", "NRW", "SPD", "Alfons-Reimund", "Hubbeldubbel")


def test_person_AttrDisplay(capsys, attrdisplay_fixture):
    # pylint: disable=W0612, W0613

    from dataclasses import dataclass

    from person.person import AttrDisplay

    @dataclass
    class MockClass(AttrDisplay):
        a: str
        b: str
        c: str

    var_1 = "späm"
    var_2 = "ham"
    var_3 = "ew"

    mock_instance = MockClass(var_1, var_2, var_3)
    print(mock_instance)
    captured = capsys.readouterr()

    expected = """MockClass:\na=späm\nb=ham\n\n"""

    assert expected == captured.out
