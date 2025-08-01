# @allure.id("ITCH-1")
# @allure.story("стори")
# @allure.feature("фича")
# @allure.epic("эпик")
# @allure.title("заголовок")
# @allure.description("описание")
# @allure.severity("minor") # blocker / critical / normal / minor / trivial

# def test_one():
#     with allure.step("step one"):
#         # тело функции

# Run commands
# - TO generate the report:
# pytest --alluredir=allure-results
# - TO run the generated report:
# allure serve allure-results
# Optional flag (for MacOS): --host 127.0.0.1
# - TO generate the local report:
# allure generate allure-results -o allure-report
# Optional flag (to rewrite the existing local report): --clean
# - TO run the generated local report:
# allure open allure-report
# Optional flag (for MacOS): --host 127.0.0.1