# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:20:02 2017

@author: wangq
"""

# RBPmap mapping binding sites of RNA bindinG proteins
# "http://rbpmap.technion.ac.il/"

def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



RBP_driver = webdriver.Chrome()
RBP_driver.get("http://rbpmap.technion.ac.il/")

mRNA_input = "AUGCAUGCAUGCAUGAUGAUCGAUCGAUCGUAGCUAGCUAGCUAGUAGUCGAUGCAGCAGCGAUCGAUGCUAGCGACGAUCGAUGCAUGCUAGCAUGCUAGUAGCGAUGCUAGCUAGCAGCGAUCGAUGCAUGCUA"  #Test value needs to be modified later


# The following is to find the text field and input sequence
mRNA_input_Xpath = "//textarea"
mRNA_input_Field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(mRNA_input_Xpath))
mRNA_input_Field.clear()
mRNA_input_Field.send_keys(mRNA_input)
# send the input in the text box


mode_Xpath = "//*[@id=\"motifs_block\"]/div[1]/div[2]/div[2]/input[1]"
mode_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(mode_Xpath))
mode_field.click()
# click the mode selection


click_here_Xpath = "//*[@id=\"motifs_block\"]/div[1]/div[2]/div[2]/a"
click_here_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(click_here_Xpath))
click_here_field.click()
#click the "click here" button


RBP_driver.switch_to_window(RBP_driver.window_handles[1])
choose_RBP_Xpath = "/html/body/form/table/tbody/tr[2]/td/div[1]/input"
choose_RBP_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(choose_RBP_Xpath))
choose_RBP_field.click()
# click the "Human" RBPs in the new window


submit_RBP_Xpath = "/html/body/form/table/tbody/tr[4]/td/input"
submit_RBP_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(submit_RBP_Xpath))
submit_RBP_field.click()
# click submit button


RBP_driver.switch_to_window(RBP_driver.window_handles[0])
submit_analysis_Xpath = "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[6]/td/input[1]"
#submit_analysis_Xpath = "(//input[@value])[14]"
submit_analysis_field = WebDriverWait(RBP_driver,10).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(submit_analysis_Xpath))
submit_analysis_field.click()
#click the submit button for the analysis


view_result_Xpath = "/html/body/table/tbody/tr[2]/td[2]/div[8]/div[3]/a"
view_result_field = WebDriverWait(RBP_driver,60).until(lambda RBP_driver: RBP_driver.find_element_by_xpath(view_result_Xpath))
print ("RNA binding protein site analysis in progress ------")
print ("This process should take less than 1 minute.")
# waiting for the result for at most 1 minute(s), could be modified
view_result_field.click()


table_Xpath = "(//table)[3]"
RBP_initial_table = WebDriverWait(RBP_driver,30).until(lambda RBP_driver: RBP_driver.find_elements_by_xpath(table_Xpath))
RBP_rearranged_table = [x.text for x in RBP_initial_table][0]  # String we want
nicer_table = RBP_rearranged_table.split("\n")
#nicer_table2 = remove_values_from_list(nicer_table, 'Position Motif Occurrence Z-score P-value')