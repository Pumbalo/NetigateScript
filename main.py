from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


hemsida = input('Länk till hemsidan?')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome()
driver.get(hemsida)
knapp = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
time.sleep(0.3)
questOne = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[3]/td[11]/input').click()
finish = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
questTwo = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[3]/td[11]/input').click()
questThree = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[4]/td[11]/input').click()
finish = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
questFour = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[3]/td[11]/input').click()
questFive = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[4]/td[11]/input').click()
finish = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
questSix = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[3]/td[11]/input').click()
questSeven = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[4]/td[11]/input').click()
questEight = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[5]/td[11]/input').click()
questNine = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[6]/td[11]/input').click()
finish = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
questTen = driver.find_element_by_xpath(
    '/html/body/form[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[3]/td[11]/input').click()

finish = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
finish = driver.find_element_by_xpath(
    '//*[@id="Forwardbutton_standardbutton1"]').click()
