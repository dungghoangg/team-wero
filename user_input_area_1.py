#input: cau tra loi cua nguoi dung
#output : 1 mang chua 5 dap an cua nguoi dung
# yeu cau : kiem tra input co phai la 1 dia danh hay khong, chi nhan input la 1 dia danh

result = []
index = 0
cities = ['an giang','ba ria-vung tau','bac giang','bac kan','bac lieu','bac ninh','ben tre','binh dinh','binh duong','binh phuoc','binh thuan','ca mau','can tho','cao bang','da nang','dak lak','dak nong','dien bien','dong nai', 'dong thap','gia lai','ha giang','ha nam','ha noi','hai duong','ha tinh','hai duong','hai phong','hau giang','hoa binh','ho chi minh','hung yen','khanh hoa','kien giang','kon tum','lai chau','lam dong','lang son','lao cai','long an','nam dinh','nghe an','ninh binh','ninh thuan','phu tho','phu yen','quang binh','quang nam','quang ngai','quang ninh','quang tri','soc trang','son la','tay ninh','thai binh','thai nguyen','thanh hoa','thua thien hue','tien giang','tra vinh','tuyen quang','vinh long','vinh phuc','yen bai']
while index < 5:
    n = input("Nhap dap an cua ban: ")
    index += 1
    n = n.lower()
    ok = 0 
    if n in cities:        
        ok = 1
    if  ok == 1:
        result.append(n)
        if len(result)== 5:
            break
        
    else:
        index -= 1
        print('khong tim thay')
        
print(result)
