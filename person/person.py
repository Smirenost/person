# person.py
import gender_guesser.detector as sex
from dataclasses import dataclass, field
from typing import List


# https://gist.github.com/jhazelwo/86124774833c6ab8f973323cb9c7e251
# class QuietError(Exception):
#     pass
#
#
# def quiet_hook(kind, message, traceback):
#     if QuietError in kind.__bases__:
#         print(f'{kind.__name__} : {message}')
#     else:
#         sys.__excepthook__(kind, message, traceback)
#
#
# sys.excepthook = quiet_hook


class NotInRange(Exception):
    pass


class TooManyFirstNames(Exception):
    def __init__(self, message):
        print(message)


class AttrDisplay:
    '''
    Mark Lutz, Programming Python
    Provides an inheritable display overload method that shows instances
    with their class names and a name=value pair for each attribute stored
    on the instance itself (but not attrs inherited from its classes). Can
    be mixed into any class, and will work on any instance.
    '''
    def gatherAttrs(self) -> list:
        attrs = []
        for key in sorted(self.__dict__):
            if self.__dict__[key] and self.__dict__[key] not in ['unknown',
                                                                 'ew', None]:
                attrs.append(f'{key}={getattr(self, key)}')
        return attrs

    def __str__(self) -> str:
        comp_repr = (f'{self.__class__.__name__}:\n' +
                     '\n'.join(str(attr) for attr in self.gatherAttrs()) + '\n')
        return comp_repr


@dataclass
class _Name_default:
    middle_name_1: str = field(default=None)
    middle_name_2: str = field(default=None)
    maiden_name: str = field(default=None)
    divorcée: str = field(default=None)


@dataclass
class _Name_base:
    first_name: str
    last_name: str


@dataclass
class Name(_Name_default, _Name_base, AttrDisplay):
    def __post_init__(self):
        first_names = self.first_name.split(' ')
        self.first_name = first_names[0]
        if len(first_names) == 2:
            self.middle_name_1 = first_names[1]
        if len(first_names) == 3:
            self.middle_name_1 = first_names[1]
            self.middle_name_2 = first_names[-1]
        if len(first_names) > 3:
            print(first_names)
            raise TooManyFirstNames("There are more than three first names!")


@dataclass
class _Peertitle_default:
    peer_title: str = field(default=None)
    peer_preposition: str = field(default=None)

    PEER_PREPOSITIONS = ['von', 'van', 'de', 'zu', 'dos', 'auf', 'der', 'und',
                         'vom', 'den']
    PEERTITLES = ['Freifrau', 'Freiherr', 'Graf', 'Gräfin', 'Herzogin',
                  'Herzog', 'Baronin', 'Baron', 'Erzherzog', 'Erzherzogin',
                  'Großherzog', 'Großherzogin', 'Kurfürst', 'Kurfürstin',
                  'Landgraf', 'Landgräfin', 'Pfalzgraf', 'Pfalzgräfin',
                  'Fürst', 'Fürstin', 'Markgraf', 'Markgräfin', 'Ritter',
                  'Edler', 'Junker', 'Landmann']

    def title(self) -> str:
        if self.peer_title is not None:
            titles = self.peer_title.split(' ')
            peer_title = ''
            peer_preposition = ''
            for prep in titles:
                if prep.lower() in self.PEER_PREPOSITIONS:
                    peer_preposition = peer_preposition + prep.lower() + ' '
                elif prep in self.PEERTITLES:
                    peer_title = peer_title + prep + ' '
            self.peer_preposition = peer_preposition.strip()
            self.peer_title = peer_title.strip()


@dataclass
class Noble(_Peertitle_default, Name, AttrDisplay):
    def __post_init__(self):
        Name.__post_init__(self)
        self.title()


@dataclass
class _Academic_title_default:
    academic_title: str = field(default=None)

    def degree_title(self) -> str:
        if self.academic_title is not None:
            if '.D' in self.academic_title:
                self.academic_title =\
                    '. '.join(c for c in self.academic_title.split('.'))
            if '.A' in self.academic_title:
                self.academic_title =\
                    '. '.join(c for c in self.academic_title.split('.'))
            if self.academic_title.endswith('Dr'):
                self.academic_title = self.academic_title[:-2] + 'Dr.'
            while '  ' in self.academic_title:
                self.academic_title = self.academic_title.replace('  ', ' ')
            self.academic_title = self.academic_title.strip()


@dataclass
class Academic(_Academic_title_default, Name, AttrDisplay):
    def __post_init__(self):
        Name.__post_init__(self)
        self.degree_title()


@dataclass
class _Person_default:
    gender: str = field(default='unknown')
    born: str = field(default='unknown')
    age: str = field(default='unknown')
    deceased: str = field(default='unknown')

    def get_sex(self) -> str:
        if '-' in self.first_name:
            first_name = self.first_name.split('-')[0]
        else:
            first_name = self.first_name
        d = sex.Detector()
        gender = d.get_gender(f'{first_name}')
        if 'female' in gender:
            self.gender = 'female'
        elif 'male' in gender:
            self.gender = 'male'

    def get_age(self) -> str:
        from datetime import date
        if self.born != 'unknown':
            if len(self.born) > 4:
                self.deceased = self.born.strip()[5:]
                self.born = self.born[:4]
            else:
                today = date.today()
                self.age = str(int(today.year) - int(self.born.strip()))


@dataclass
class Person(_Peertitle_default, _Academic_title_default, _Person_default,
             Name, AttrDisplay):
    def __post_init__(self):
        Name.__post_init__(self)
        Academic.__post_init__(self)
        self.get_sex()
        self.get_age()


@dataclass
class _Politician_default:
    electoral_ward: str = field(default='ew')
    ward_no: int = field(default=None)
    voter_count: int = field(default=None)
    minister: str = field(default=None)
    offices: List[str] = field(default_factory=lambda: [])
    party: str = field(default=None)
    parties: List[str] = field(default_factory=lambda: [])

    def renamed_wards(self):
        renamed_wards = ["Kreis Aachen I", "Hochsauerlandkreis II – Soest III",
                         "Kreis Aachen II"]
        wards = {"Kreis Aachen I": "Aachen III",
                 "Hochsauerlandkreis II – Soest III": "Hochsauerlandkreis II",
                 "Kreis Aachen II": "Aachen IV" if self.last_name in
                 ["Wirtz", "Weidenhaupt"] else "Kreis Aachen I"}
        if self.electoral_ward in renamed_wards:
            self.electoral_ward = wards[self.electoral_ward]

    def scrape_wiki_for_ward(self):
        from bs4 import BeautifulSoup
        import requests

        URL_base = 'https://de.wikipedia.org/wiki/Landtagswahlkreis_{}'
        URL = URL_base.format(self.electoral_ward)
        req = requests.get(URL)
        bsObj = BeautifulSoup(req.text, 'lxml')
        table = bsObj.find(class_='infobox float-right toptextcells')
        for td in table.find_all('td'):
            if 'Wahlkreisnummer' in td.text:
                ward_no = td.find_next().text.strip()
                ward_no = ward_no.split(' ')[0]
                self.ward_no = int(ward_no)
            elif 'Wahlberechtigte' in td.text:
                voter_count = td.find_next().text.strip()
                if voter_count[-1] == ']':
                    voter_count = voter_count[:-3]
                if ' ' in voter_count:
                    voter_count = ''.join(voter_count.split(' '))
                elif '.' in voter_count:
                    voter_count = ''.join(voter_count.split('.'))
                self.voter_count = int(voter_count)


@dataclass
class Politician(_Peertitle_default, _Academic_title_default, _Person_default,
                 _Politician_default, Name, AttrDisplay):

    def __post_init__(self):
        Name.__post_init__(self)
        Academic.__post_init__(self)
        Noble.__post_init__(self)
        _Person_default.get_sex(self)
        _Person_default.get_age(self)
        if self.electoral_ward not in ['ew', 'Landesliste']:
            self.renamed_wards()
            self.scrape_wiki_for_ward()
        else:
            self.electoral_ward = "ew"
        if self.party and self.party not in self.parties:
            self.parties.append(self.party)
        if self.minister and self.minister not in self.offices:
            self.offices.append(self.minister)


@dataclass
class _MdL_default:
    parl_pres: bool = field(default=False)
    parl_vicePres: bool = field(default=False)


@dataclass
class _MdL_base:
    legislature: int


@dataclass
class MdL(_MdL_default, Politician, _MdL_base, AttrDisplay):
    def __post_init__(self):
        if int(self.legislature) not in range(10, 21):
            raise NotInRange('Number for legislature not in range')
        Politician.__post_init__(self)
