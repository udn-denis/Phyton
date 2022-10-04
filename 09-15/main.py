import wmi

pc = wmi.WMI()

pcInfoDevice = pc.Win32_SystemDevices()

pcInfoProduct = pc.CIM_Product()

# # print(pcInfo)
# # for inf in pcInfoProduct:
# # 	print(inf)
#
# help(print)
#
# # with open("device.csv", "w", encoding="utf-8") as fdev:
# # 	fdev.write("Caption,Name,Description,DeviceID\n")
# # 	for dev in pcInfoDevice:
# # 		fdev.write(f"{dev.PartComponent.Caption},{dev.PartComponent.Name},{dev.PartComponent.Description},{dev.PartComponent.DeviceID}\n")
# #
# # with open("product.csv", "w", encoding="utf-8") as fprod:
# # 	fprod.write("Caption,Name,Description,InstallSource\n")
# # 	count = 0
# # 	for prod in pcInfoProduct:
# # 		count += 1
# # 		try:
# # 			fprod.write(f"{prod.Caption},{prod.Name},{prod.Description},{prod.LocalPackage}\n")
# # 		except:
# # 			count += 1
# # 	print(f"Количество ошибок: {count}")