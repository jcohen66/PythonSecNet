protocolList = ["FTP", "HTTP", "SNMP", "SSH"]
element_to_find = "SSH"
for i in range(len(protocolList)):
    if protocolList[i] == element_to_find:
        print("Element found at index", i)
        break


