This is a project with is used 
BDD
playwright
Report Allure 

testing https://medium.com/@antonio.uxcreator/step-by-step-playwright-with-behave-bdd-and-allure-reports-implementation-tutorial-34dbe2ff009a


run test via behave
'''
behave features/cart.feature -f allure_behave.formatter:AllureFormatter -o reports/allure-results
'''

run test in bug mode step by step
'''
python -m pdb -m behave features/cart.feature
'''

run Allure report
'''
allure serve reports/allure-results
'''
