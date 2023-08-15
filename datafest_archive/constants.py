from datafest_archive.models.website.configuration import MenuItem

CONTENT_DIRECTORY = "content"
CONTENT_EDITION_DIRECTORY = "editions"
CONTENT_PEOPLE_DIRECTORY = "authors"
CONTENT_PROJECT_DIRECTORY = "projects"
CONFIG_DIRECTORY = "config"
INDEX_REGULAR_PAGE = "index.md"
INDEX_LIST_PAGE = "_index.md"
FEATURED_TAG = "featured"
MENUS_FILE_NAME = "menus.yaml"

ROLE_ADVISOR = "Advisor"
ROLE_STUDENT = "Student"

DATE_YEAR_FORMAT = "%Y"
DATE_YEAR_MONTH_DAY_FORMAT = "%Y-%m-%d"

WINTER = "Winter"
SPRING = "Spring"
SUMMER = "Summer"
FALL = "Fall"

# Menu items for the main menu

info_for_advisors = MenuItem(
    name="Info for Advisors", url="info-advisors", weight=1, parent=None
)
info_for_students = MenuItem(
    name="Info for Students", url="info-students", weight=2, parent=None
)
projects = MenuItem(name="Projects", url="projects", weight=3, parent=None)
people = MenuItem(name="People", url="people", weight=4, parent=None)
contact = MenuItem(name="Contact", url="contact", weight=6, parent=None)
