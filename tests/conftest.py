# conftest.py
# import builtins
# import io
import logging

# import os
import pytest

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def toomanyfirstnames_fixture():
    LOGGER.info("Setting Up TooManyFirstNames Fixture ...")
    yield
    LOGGER.info("Tearing Down TooManyFirstNames Fixture ...")


@pytest.fixture(scope="function")
def name_fixture():
    LOGGER.info("Setting Up Names Fixture ...")
    yield
    LOGGER.info("Tearing Down Names Fixture ...")


@pytest.fixture(scope="function")
def academic_fixture():
    LOGGER.info("Setting Up Academic Fixture ...")
    yield
    LOGGER.info("Tearing Down Academic Fixture ...")


@pytest.fixture(scope="function")
def noble_fixture():
    LOGGER.info("Setting Up Noble Fixture ...")
    yield
    LOGGER.info("Tearing Down Noble Fixture ...")


@pytest.fixture(scope="function")
def person_fixture():
    LOGGER.info("Setting Up Person Fixture ...")
    yield
    LOGGER.info("Tearing Down Person Fixture ...")


@pytest.fixture(scope="function")
def politician_fixture():
    LOGGER.info("Setting Up Politician Fixture ...")
    yield
    LOGGER.info("Tearing Down Politician Fixture ...")


@pytest.fixture(scope="function")
def mdl_fixture():
    LOGGER.info("Setting Up MdL Fixture ...")
    yield
    LOGGER.info("Tearing Down MdL Fixture ...")


@pytest.fixture(scope="function")
def notinrange_fixture():
    LOGGER.info("Setting Up NotInRange Fixture ...")
    yield
    LOGGER.info("Tearing Down NotInRange Fixture ...")


@pytest.fixture(scope="function")
def attrdisplay_fixture():
    LOGGER.info("Setting Up AttrDisplay Fixture ...")
    yield
    LOGGER.info("Tearing Down AttrDisplay Fixture ...")


@pytest.fixture(scope="function")
def first_names_fixture():
    LOGGER.info("Setting Up FirstNames Fixture ...")
    yield
    LOGGER.info("Tearing Down FirstNames Fixture ...")


@pytest.fixture(scope="function")
def standardize_name_fixture():
    LOGGER.info("Setting Up StandardizeName Fixture ...")
    yield
    LOGGER.info("Tearing Down StandardizeName Fixture ...")


# https://stackoverflow.com/a/51742499/6597765
# @pytest.fixture(scope="function")
# def cleanup_file_fixture(monkeypatch):
#     files = []
#     monkeypatch.setattr(builtins, 'open', patch_open(builtins.open, files))
#     monkeypatch.setattr(io, 'open', patch_open(io.open, files))
#     yield
#     for file in files:
#         os.remove(file)
