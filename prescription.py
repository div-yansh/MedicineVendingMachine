import cv2
import os
import pandas as pd 
import pytesseract

def prescription():
	df = pd.read_csv("MedicineStock.csv")

	base = os.getcwd()
	cwd = os.path.join(os.getcwd(), "img")
	os.chdir(cwd)
	
	img = next(os.walk(os.getcwd()))[2][0]
	strr = pytesseract.image_to_string(img)
	strr = strr.strip().strip("\n").strip().strip("\n")
	strr = strr.split("\n")
	os.remove(img)

	medicine = []
	price = []
	category = []
	for pres in strr:
		for med, prc in zip(df.iloc[:, 0], df.iloc[:, 3]):
			count = 0
			for cm, cp in zip(med.lower(), pres.lower()):
				if cm == cp:
					count += 1
			if count >= 4:
				medicine.append(med)
				price.append(prc)
	medicine = list(set(medicine))

	os.chdir(base)
	
	return medicine, price, round(sum(price), 2)		
	

	