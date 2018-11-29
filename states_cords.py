text = '''Telangana, India	17.123184	79.208824
Madhya Pradesh, India	23.473324	77.947998
Haryana, India	29.238478	76.431885
Chhattisgarh, India	21.295132	81.828232
Haryana, India	29.065773	76.040497
Bhitarwar, Madhya Pradesh, India	25.794033	78.116531
Maharashtra, India	19.601194	75.552979
Tripura, India	23.745127	91.746826
Chandoor, Telangana, India	17.874857	78.100815
Karnataka, India	15.317277	75.713890
Kerala, India	10.850516	76.271080
Uttar Pradesh, India	28.207609	79.826660
Assam, India	26.244156	92.537842
Maharashtra, India	19.663280	75.300293
Tamil Nadu, India	11.127123	78.656891
Karnataka, India	15.317277	75.713890
West Bengal, India	22.978624	87.747803
Gujarat, India	22.309425	72.136230
Odisha, India	20.940920	84.803467
Rajasthan, India	27.391277	73.432617
Himachal Pradesh, India	32.084206	77.571167'''

csv = text.split('\n')
data = ""
dic = dict()
for x in csv:
    dic[x.split("\t")[0].split(",")[0] ] =str(x.split("\t")[1]) +","+ str( x.split("\t")[2])
    #print(x.split("\t"))


print("***************************")
print(dic)
