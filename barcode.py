itemList = {"xxxxxxxxxxx":{"item":"PSP","price":1000}
}

while True:
	print("Scan your barcode => ")
	value = input()
	print(value)
	if value=="exit":
		break

	for key in itemList.keys():
		if key==value:
			print("Item details => ",itemList[key])
			break
	else:
		print("No items for this barcode :(",value)
