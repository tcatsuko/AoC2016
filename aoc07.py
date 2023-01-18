import re

f = open('aoc07.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
TLS_valid_ip = []
SSL_valid_ip = []

def check_abba(text):
    if len(text) >= 4:
        for counter in range(len(text) - 3):
            a = text[counter]
            b = text[counter + 1]
            c = text[counter + 2]
            d = text[counter + 3]
            if (a != b) and (c != d) and (a == d) and (b == c):
                return True
    return False
def check_aba(text):
    found_aba = []
    if len(text) >= 3:
        for counter in range(len(text) - 2):
            a = text[counter]
            b = text[counter + 1]
            c = text[counter + 2]
            if (a == c):
                found_aba += [text[counter:counter+3]]
    return found_aba
def check_bab(aba, text):
    for item in aba:
        bab = item[1] + item[0] + item[1]
        if bab in text:
            return True
    return False

for line in raw_input:
    supports_TLS = False
    # get text inside of brackets
    hyper_text = re.findall(r'\[.*?\]', line)
    cleaned_line = line[:]
    for item in hyper_text:
        cleaned_line = cleaned_line.replace(item, ' ')
    split_line = cleaned_line.split(' ')
    hyper_check = False
    outside_abba = False
    aba = False
    bab = False
    found_aba = []
    valid_ssl = False
    for item in split_line:
       
        abba_test = check_abba(item)
        if abba_test == True and outside_abba == False:
            outside_abba = True
            break
    for item in hyper_text:
        hyper_test = check_abba(item[1:-1])
        if hyper_test == True and hyper_check == False:
            hyper_check = True
            break
    for item in split_line:
        found_aba += check_aba(item)
    for item in hyper_text:
        valid_ssl = check_bab(found_aba, item)
        if valid_ssl == True:
            break

    if (valid_ssl) == True:
        SSL_valid_ip += [line]
    if (outside_abba == True) and (hyper_check == False):
        TLS_valid_ip += [line]
    
print('Part 1: There are ' + str(len(TLS_valid_ip)) + ' valid TLS IPs')
# 77 wrong
print('Part 2: there are ' + str(len(SSL_valid_ip)) + ' SSL valid IPs')