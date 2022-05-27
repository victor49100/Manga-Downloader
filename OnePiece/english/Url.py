#11 04 90 00 = 1049
#11 04 00 00 = 1040
#10 99 90 00 = 999
#10 10 00 00 = 100
#10 01 00 00 = 10
#10 00 10 00 = 1
#l1 l2 l3 XX
#https://cdn.readonepiece.com/file/mangap/2/10110000/1.jpeg

def ConvertUrlToTome (tome):
    l1 = "10"
    l2 = "00"
    l3 = "00"
    if tome < 10:
        l3 = (str(tome)+"0")
        t = (str(l1)+str(l2)+str(l3)+"00")
        return ("https://cdn.readonepiece.com/file/mangap/2/"+str(t)+"/X.jpeg")

    if tome > 9 and tome <100:
        d =  int(str(tome)[:1])
        l2 = ("0"+str(d))
        l3 = (str(tome%10)+"0")
        print (l1,l2,l3)
        t = (str(l1)+str(l2)+str(l3)+"00")
        return ("https://cdn.readonepiece.com/file/mangap/2/"+str(t)+"/X.jpeg")

    if tome > 99 and tome < 1000:
        l2 = str(tome)[:2]
        l3 = (str(tome%10)+"0")
        t = (str(l1)+str(l2)+str(l3)+"00")
        print ("https://cdn.readonepiece.com/file/mangap/2/"+str(t)+"/X.jpeg")
    if tome > 999 and tome < 1050:
            l1 = "11"
            l2 = str(tome)[1:3]
            l3 = (str(tome%10)+"0")
            t = (str(l1)+str(l2)+str(l3)+"00")
            return ("https://cdn.readonepiece.com/file/mangap/2/"+str(t)+"/X.jpeg")
    if tome > 1049:
        t = tome
        return ("https://cdn.readonepiece.com/file/CDN-M-A-N/op_tcb_"+str(t)+"_X.png")
