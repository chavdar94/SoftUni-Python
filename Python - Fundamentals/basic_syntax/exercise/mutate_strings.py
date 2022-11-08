str1 = input()
str2 = input()
m_str = ''
for i in range(len(str1)):
    f_string = str1[i+1:]
    m_str = str2[:i+1]+f_string
    if str1[i] != str2[i]:
        print(m_str)