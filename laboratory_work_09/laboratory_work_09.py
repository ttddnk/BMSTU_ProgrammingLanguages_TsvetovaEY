import re
#1
text1="17.10.26, пампампам 12.12.22, 13.11.2030, пупупу"
t1 = re.findall(r"(\d{2}\.\d{2}\.(?:\d{4}|\d{2}))", text1)
print(t1)

#2
text2="22.28 часов ночи, потом будет 22:29"
t2 = re.findall(r"\d{2}[.:]\d{2}", text2)
print(t2)

#3
text3="8, 800, -555, 35-35 +777 and kotiki"
t3 = re.findall(r"[+-]?\d+", text3)
print(t3)

#4
text4 = "66 98,7 3.14 -88 +67vibe minus 52"
t4 = re.findall(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)", text4)
print(t4)

