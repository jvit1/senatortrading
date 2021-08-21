from selenium import webdriver
import pandas as pd
import time

# Time management
start_time = time.time()

website = "https://efdsearch.senate.gov/"
browser = webdriver.Chrome('C:/Users/student/Documents/Python/chromedriver.exe')
browser.maximize_window()
browser.get(website)

# Agree to terms and conditions
browser.find_element_by_xpath("//*[@id='agree_statement']").click()
time.sleep(1)
# Set search criteria, in this case we are searching for senate periodic transactions
browser.find_element_by_xpath(
    "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'form-check-input', ' ' ))]").click()
browser.find_element_by_xpath('//*[@id="filerTypes"]').click()
browser.find_element_by_xpath("//*[@id='reportTypeLabelPtr']").click()
time.sleep(1)
# Hit the search button
browser.find_element_by_xpath("//*[@id='searchForm']/div/button").click()


# Creating dataframe
data = {'Name': [], 'Transaction Date': [], 'Owner': [], 'Ticker': [],
        'Asset Name': [], 'Asset Type': [], 'Type': [], 'Amount': [], 'Comment': []}
df = pd.DataFrame(data)

time.sleep(1)
pagenumber = (browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "current", " " ))]')).text
pagenumber = int(pagenumber)
finalpage = (browser.find_element_by_xpath('//*[@id="filedReports_paginate"]/span/a[6]')).text
finalpage= int(finalpage)

while pagenumber <= finalpage - 4:
    count = 1
    while count <= 25: # Has to be <= 25 to loop through page
        time.sleep(2)
        caps = str(browser.find_element_by_xpath('//*[@id="filedReports"]/tbody/tr[' + str(count) + ']/td[1]').text)
        testcaps = caps.isupper()
        if testcaps == False:
            button = browser.find_element_by_xpath('/html/body/div[1]/main/div/div/div[6]/div/div/div/table/tbody/tr['
                                                   + str(count) + ']/td[4]/a')
            browser.execute_script("arguments[0].click();", button)
            time.sleep(2)
            browser.switch_to.window(browser.window_handles[1])
        # elif testcaps == True:
        #     print("Handwritten document, unable to scrape.")
        #     count = count + 1


            individual = 1
            while individual <= int(
                    browser.find_element_by_xpath('//*[@id="content"]/div/div/section/div/div/table/tbody/tr[1]/td[1]').text):
                # 36) Finds the number of transactions per report and cycles until individual hits that number.
                df.loc[-1] = {'Name': browser.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div[1]/h2').text,
                              'Transaction Date': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(individual) + ']/td[2]').text,
                              'Owner': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[3]').text,
                              'Ticker': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[4]').text,
                              'Asset Name': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[5]').text,
                              'Asset Type': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[6]').text,
                              'Type': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[7]').text,
                              'Amount': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[8]').text,
                              'Comment': browser.find_element_by_xpath(
                                  '//*[@id="content"]/div/div/section/div/div/table/tbody/tr[' + str(
                                      individual) + ']/td[9]').text
                              }
                individual = individual + 1
                df.index = df.index + 1
                df = df.sort_index()
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            # Print the output.
            print(df.head())
            print(len(df.index))
            count = count + 1
        else:
            count = count + 1
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element_by_xpath('/html/body/div[1]/main/div/div/div[6]/div/div/div/div[3]/div[2]/div/a[2]').click()
    pagenumber = pagenumber+1

df.to_csv(r'C:\Users\student\Documents\Python\CongressInvestments2.csv', index=False)
