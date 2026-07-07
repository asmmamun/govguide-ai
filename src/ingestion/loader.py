
import os

file_path = "data/raw/shorkari_kormochari_sringkhola_o_appeal_bidhimala_2018.txt"
with open(file_path, encoding='utf-8') as doc:
    text = doc.read()
print(text)

