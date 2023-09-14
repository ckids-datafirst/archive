from datafest_archive.utils import (
    full_name_to_first_and_last_name,
    people_name_to_directory_name,
    sanitanize_name,
)


def test_sanitaze_name():
    assert sanitanize_name("maximiliano") == "maximiliano"
    assert sanitanize_name("Maximiliano") == "Maximiliano"
    assert sanitanize_name("Jose-Luis") == "Jose-Luis"
    assert sanitanize_name("Andrés") == "Andres"


def test_people_name_to_directory_name():
    assert people_name_to_directory_name("Maximiliano Osorio") == "maximiliano-osorio"
    assert people_name_to_directory_name("Jose-Luis Ambite") == "jose-luis-ambite"
    assert people_name_to_directory_name("Carlos Buil-Aranda") == "carlos-buil-aranda"
    # Jianing (Julia) Chen
    assert people_name_to_directory_name("Jianing (Julia) Chen") == "jianing-julia-chen"
    # Daniel E. O’Leary
    assert people_name_to_directory_name("Daniel E. O’Leary") == "daniel-e-oleary"
    assert (
        people_name_to_directory_name("Maximiliano Federico Osorio Banados")
        == "maximiliano-federico-osorio-banados"
    )
    assert (
        people_name_to_directory_name("Maximiliano Osorio Banados")
        == "maximiliano-osorio-banados"
    )
    assert people_name_to_directory_name("Maximiliano") == "maximiliano"


def test_full_name_to_first_and_last_name():
    assert full_name_to_first_and_last_name("Maximiliano Osorio") == (
        "Maximiliano",
        "Osorio",
    )
    assert full_name_to_first_and_last_name("Jose-Luis Ambite") == (
        "Jose-Luis",
        "Ambite",
    )
    assert full_name_to_first_and_last_name("Carlos Buil-Aranda") == (
        "Carlos",
        "Buil-Aranda",
    )
    assert full_name_to_first_and_last_name("Maximiliano Federico Osorio Banados") == (
        "Maximiliano Federico",
        "Osorio Banados",
    )
    assert full_name_to_first_and_last_name("Maximiliano") == ("Maximiliano", "")
    assert full_name_to_first_and_last_name("Maximiliano Osorio Banados") == (
        "Maximiliano",
        "Osorio Banados",
    )
    # Muhammad Oneeb Ul Haq Kha
    assert full_name_to_first_and_last_name("Muhammad Oneeb Ul Haq Kha") == (
        "Muhammad Oneeb",
        "Ul Haq Kha",
    )
