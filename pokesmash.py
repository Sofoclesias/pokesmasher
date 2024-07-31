import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import warnings
import time
warnings.filterwarnings('ignore')

url = 'https://pokesmash.xyz/'

options = Options()
# options.add_argument("--headless")
options.set_preference('permissions.default.image', 1)

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(300)
driver.get(url)
driver.maximize_window()

pokemon = {
    'name':[],
    'pass':[],
    'smash':[]
}

time.sleep(3)

for i in range(1,1026):
    if i==1:
        pass
    else:
        pokemon['name'] += [driver.find_element(By.XPATH, '//span[contains(text(), "What Others Chose for")]/span').text]
        pokemon['pass'] += [int(driver.find_element(By.XPATH, '//span[text()="Passes"]/parent::div/span[2]').text)]
        pokemon['smash'] += [int(driver.find_element(By.XPATH, '//span[text()="Smashes"]/parent::div/span[2]').text)]

        print(f"""Pokémon: {pokemon['name'][i-2]}. Passes: {pokemon['pass'][i-2]}; Smashes: {pokemon['smash'][i-2]}""")
            
    pass_btm = driver.find_element(By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root pass ButtonUnstyled-root css-1j5o1sy"]')
    pass_btm.click()
    time.sleep(3)
    
pokemon['name'] += ['Pecharunt']
pokemon['pass'] += [13164]
pokemon['smash'] += [2067]

driver.close()

pokesmash = pd.DataFrame(pokemon)
pokesmash.to_csv('pokesmash.csv',index=False)

