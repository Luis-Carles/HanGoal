#Dependencies
import jamotools as jt


#Calcule Methods for numbers Exam

def calculateDate (y,m,d):

    year = y
    month = m
    day = d
    answer = [['',''],['',''],['','']]

    if (y<2000):
        answer[0][0] = '천구백'
        answer[0][1] = 'cheongubaek'
        year = year - 1900

    if(y>=2000): 
        answer[0][0] = '이천'
        answer[0][1] = 'icheon'
        year = year - 2000 

    if(9 < year < 20):
        answer[0][0] = answer[0][0] + '십'
        answer[0][1] = answer[0][1] + 'sib'
        year = year - 10

    if(19 < year < 30):
        answer[0][0] = answer[0][0] + '이십'
        answer[0][1] = answer[0][1] + 'isib'
        year = year - 20 

    if(29 < year < 40):
        answer[0][0] = answer[0][0] + '삼십'
        answer[0][1] = answer[0][1] + 'samsib'
        year = year - 30 

    if(39 < year < 50):
        answer[0][0] = answer[0][0] + '사십'
        answer[0][1] = answer[0][1] + 'sasib'
        year = year - 40

    if(49 < year < 60):
        answer[0][0] = answer[0][0] + '오십'
        answer[0][1] = answer[0][1] + 'osib'
        year = year - 50

    if(59 < year < 70):
        answer[0][0] = answer[0][0] + '육십'
        answer[0][1] = answer[0][1] + 'yuksib'
        year = year - 60

    if(69 < year < 80):
        answer[0][0] = answer[0][0] + '칠십'
        answer[0][1] = answer[0][1] + 'chilsib'
        year = year - 70

    if(79 < year < 90):
        answer[0][0] = answer[0][0] + '팔십'
        answer[0][1] = answer[0][1] + 'palsib'
        year = year - 80

    if(89 < year < 100):
        answer[0][0] = answer[0][0] + '구십'
        answer[0][1] = answer[0][1] + 'gusib'
        year = year - 90

    if(0 < year < 10):
        if(year == 1):
            answer[0][0] = answer[0][0] + '일'
            answer[0][1] = answer[0][1] + 'il'
            year = year - 1

        if(year == 2):
            answer[0][0] = answer[0][0] + '이'
            answer[0][1] = answer[0][1] + 'i'
            year = year - 2

        if(year == 3):
            answer[0][0] = answer[0][0] + '삼'
            answer[0][1] = answer[0][1] + 'sam'
            year = year - 3

        if(year == 4):
            answer[0][0] = answer[0][0] + '사'
            answer[0][1] = answer[0][1] + 'sa'
            year = year - 4

        if(year == 5):
            answer[0][0] = answer[0][0] + '오'
            answer[0][1] = answer[0][1] + 'o'
            year = year - 5

        if(year == 6):
            answer[0][0] = answer[0][0] + '육'
            answer[0][1] = answer[0][1] + 'yuk'
            year = year - 6

        if(year == 7):
            answer[0][0] = answer[0][0] + '칠'
            answer[0][1] = answer[0][1] + 'chil'
            year = year - 7

        if(year == 8):
            answer[0][0] = answer[0][0] + '팔'
            answer[0][1] = answer[0][1] + 'pal'
            year = year - 8

        if(year == 9):
            answer[0][0] = answer[0][0] + '구'
            answer[0][1] = answer[0][1] + 'gu'
            year = year - 9

    if(0 < month < 13):
        if(month == 1):
            answer[1][0] = answer[1][0] + '일'
            answer[1][1] = answer[1][1] + 'il'

        if(month == 2):
            answer[1][0] = answer[1][0] + '이'
            answer[1][1] = answer[1][1] + 'i'

        if(month == 3):
            answer[1][0] = answer[1][0] + '삼'
            answer[1][1] = answer[1][1] + 'sam'

        if(month == 4):
            answer[1][0] = answer[1][0] + '사'
            answer[1][1] = answer[1][1] + 'sa'

        if(month == 5):
            answer[1][0] = answer[1][0] + '오'
            answer[1][1] = answer[1][1] + 'o'

        if(month == 6):
            answer[1][0] = answer[1][0] + '유'
            answer[1][1] = answer[1][1] + 'yu'

        if(month == 7):
            answer[1][0] = answer[1][0] + '칠'
            answer[1][1] = answer[1][1] + 'chil'

        if(month == 8):
            answer[1][0] = answer[1][0] + '팔'
            answer[1][1] = answer[1][1] + 'pal'

        if(month == 9):
            answer[1][0] = answer[1][0] + '구'
            answer[1][1] = answer[1][1] + 'gu'

        if(month == 10):
            answer[1][0] = answer[1][0] + '시'
            answer[1][1] = answer[1][1] + 'si'

        if(month == 11):
            answer[1][0] = answer[1][0] + '십일'
            answer[1][1] = answer[1][1] + 'sibil'

        if(month == 12):
            answer[1][0] = answer[1][0] + '십이'
            answer[1][1] = answer[1][1] + 'sibi'

    if(0 < day < 32):
        if(29 < day < 32):
            answer[2][0] = answer[2][0] + '삼십'
            answer[2][1] = answer[2][1] + 'samsib'
            day = day - 30
            
        if(19 < day < 30):
            answer[2][0] = answer[2][0] + '이십'
            answer[2][1] = answer[2][1] + 'isib'
            day = day - 20

        if(9 < day < 20):
            answer[2][0] = answer[2][0] + '십'
            answer[2][1] = answer[2][1] + 'sib'
            day = day - 10

        if(day == 1):
            answer[2][0] = answer[2][0] + '일'
            answer[2][1] = answer[2][1] + 'il'

        if(day == 2):
            answer[2][0] = answer[2][0] + '이'
            answer[2][1] = answer[2][1] + 'i'

        if(day == 3):
            answer[2][0] = answer[2][0] + '삼'
            answer[2][1] = answer[2][1] + 'sam'

        if(day == 4):
            answer[2][0] = answer[2][0] + '사'
            answer[2][1] = answer[2][1] + 'sa'

        if(day == 5):
            answer[2][0] = answer[2][0] + '오'
            answer[2][1] = answer[2][1] + 'o'

        if(day == 6):
            answer[2][0] = answer[2][0] + '육'
            answer[2][1] = answer[2][1] + 'yuk'

        if(day == 7):
            answer[2][0] = answer[2][0] + '칠'
            answer[2][1] = answer[2][1] + 'chil'

        if(day == 8):
            answer[2][0] = answer[2][0] + '팔'
            answer[2][1] = answer[2][1] + 'pal'

        if(day == 9):
            answer[2][0] = answer[2][0] + '구'
            answer[2][1] = answer[2][1] + 'gu'

    return answer

def calculateTime(h,min,sec):

    hour = h
    minutes = min
    seconds = sec
    answer = [['',''],['',''],['','']]

    if(hour==1):
        answer[0][0] = answer[0][0] + '한'
        answer[0][1] = answer[0][1] + 'han'

    if(hour==2):
        answer[0][0] = answer[0][0] + '두'
        answer[0][1] = answer[0][1] + 'du'

    if(hour==3):
        answer[0][0] = answer[0][0] + '세'
        answer[0][1] = answer[0][1] + 'se'

    if(hour==4):
        answer[0][0] = answer[0][0] + '네'
        answer[0][1] = answer[0][1] + 'ne'

    if(hour==5):
        answer[0][0] = answer[0][0] + '다섯'
        answer[0][1] = answer[0][1] + 'daseot'

    if(hour==6):
        answer[0][0] = answer[0][0] + '여섯'
        answer[0][1] = answer[0][1] + 'yeoseot'

    if(hour==7):
        answer[0][0] = answer[0][0] + '이곱'
        answer[0][1] = answer[0][1] + 'ilgob'

    if(hour==8):
        answer[0][0] = answer[0][0] + '여덟'
        answer[0][1] = answer[0][1] + 'yeodeolb'

    if(hour==9):
        answer[0][0] = answer[0][0] + '아홉'
        answer[0][1] = answer[0][1] + 'ahob'

    if(hour==10):
        answer[0][0] = answer[0][0] + '열'
        answer[0][1] = answer[0][1] + 'yeol'

    if(hour==11):
        answer[0][0] = answer[0][0] + '열한'
        answer[0][1] = answer[0][1] + 'yeolhan'

    if(hour==12):
        answer[0][0] = answer[0][0] + '여두'
        answer[0][1] = answer[0][1] + 'yeoldu'

    if(-1<minutes<60):
        if(9 < minutes < 20):
            answer[1][0] = answer[1][0] + '십'
            answer[1][1] = answer[1][1] + 'sib'
            minutes = minutes - 10

        if(19 < minutes < 30):
            answer[1][0] = answer[1][0] + '이십'
            answer[1][1] = answer[1][1] + 'isib'
            minutes = minutes - 20 

        if(29 < minutes < 40):
            answer[1][0] = answer[1][0] + '삼십'
            answer[1][1] = answer[1][1] + 'samsib'
            minutes = minutes - 30 

        if(39 < minutes < 50):
            answer[1][0] = answer[1][0] + '사십'
            answer[1][1] = answer[1][1] + 'sasib'
            minutes = minutes - 40

        if(49 < minutes < 60):
            answer[1][0] = answer[1][0] + '오십'
            answer[1][1] = answer[1][1] + 'osib'
            minutes = minutes - 50

        if(minutes == 1):
            answer[1][0] = answer[1][0] + '일'
            answer[1][1] = answer[1][1] + 'il'

        if(minutes == 2):
            answer[1][0] = answer[1][0] + '이'
            answer[1][1] = answer[1][1] + 'i'

        if(minutes == 3):
            answer[1][0] = answer[1][0] + '삼'
            answer[1][1] = answer[1][1] + 'sam'

        if(minutes == 4):
            answer[1][0] = answer[1][0] + '사'
            answer[1][1] = answer[1][1] + 'sa'

        if(minutes == 5):
            answer[1][0] = answer[1][0] + '오'
            answer[1][1] = answer[1][1] + 'o'

        if(minutes == 6):
            answer[1][0] = answer[1][0] + '육'
            answer[1][1] = answer[1][1] + 'yuk'

        if(minutes == 7):
            answer[1][0] = answer[1][0] + '칠'
            answer[1][1] = answer[1][1] + 'chil'

        if(minutes == 8):
            answer[1][0] = answer[1][0] + '팔'
            answer[1][1] = answer[1][1] + 'pal'

        if(minutes == 9):
            answer[1][0] = answer[1][0] + '구'
            answer[1][1] = answer[1][1] + 'gu'

    if(-1<seconds<60):
        if(9 < seconds < 20):
            answer[2][0] = answer[2][0] + '십'
            answer[2][1] = answer[2][1] + 'sib'
            seconds = seconds - 10

        if(19 < seconds < 30):
            answer[2][0] = answer[2][0] + '이십'
            answer[2][1] = answer[2][1] + 'isib'
            seconds = seconds - 20 

        if(29 < seconds < 40):
            answer[2][0] = answer[2][0] + '삼십'
            answer[2][1] = answer[2][1] + 'samsib'
            seconds = seconds - 30 

        if(39 < seconds < 50):
            answer[2][0] = answer[2][0] + '사십'
            answer[2][1] = answer[2][1] + 'sasib'
            seconds = seconds - 40

        if(49 < seconds < 60):
            answer[2][0] = answer[2][0] + '오십'
            answer[2][1] = answer[2][1] + 'osib'
            seconds = seconds - 50

        if(seconds == 1):
            answer[2][0] = answer[2][0] + '일'
            answer[2][1] = answer[2][1] + 'il'

        if(seconds == 2):
            answer[2][0] = answer[2][0] + '이'
            answer[2][1] = answer[2][1] + 'i'

        if(seconds == 3):
            answer[2][0] = answer[2][0] + '삼'
            answer[2][1] = answer[2][1] + 'sam'

        if(seconds == 4):
            answer[2][0] = answer[2][0] + '사'
            answer[2][1] = answer[2][1] + 'sa'

        if(seconds == 5):
            answer[2][0] = answer[2][0] + '오'
            answer[2][1] = answer[2][1] + 'o'

        if(seconds == 6):
            answer[2][0] = answer[2][0] + '육'
            answer[2][1] = answer[2][1] + 'yuk'

        if(seconds == 7):
            answer[2][0] = answer[2][0] + '칠'
            answer[2][1] = answer[2][1] + 'chil'

        if(seconds == 8):
            answer[2][0] = answer[2][0] + '팔'
            answer[2][1] = answer[2][1] + 'pal'

        if(seconds == 9):
            answer[2][0] = answer[2][0] + '구'
            answer[2][1] = answer[2][1] + 'gu'

    return answer

def calculateBig(p):

    price = p
    answer = ['','']

    if(9999<price<20000):
        answer[0] = answer[0] + '만'
        answer[1] = answer[1] + 'man'
        price = price - 10000

    if(19999<price<30000):
        answer[0] = answer[0] + '이만'
        answer[1] = answer[1] + 'iman'
        price = price - 20000

    if(29999<price<40000):
        answer[0] = answer[0] + '삼만'
        answer[1] = answer[1] + 'samman'
        price = price - 30000

    if(39999<price<50000):
        answer[0] = answer[0] + '사만'
        answer[1] = answer[1] + 'saman'
        price = price - 40000

    if(49999<price<60000):
        answer[0] = answer[0] + '오만'
        answer[1] = answer[1] + 'oman'
        price = price - 50000

    if(59999<price<70000):
        answer[0] = answer[0] + '육만'
        answer[1] = answer[1] + 'yukman'
        price = price - 60000

    if(69999<price<80000):
        answer[0] = answer[0] + '칠만'
        answer[1] = answer[1] + 'chilman'
        price = price - 70000  

    if(79999<price<90000):
        answer[0] = answer[0] + '팔만'
        answer[1] = answer[1] + 'palman'
        price = price - 80000

    if(89999<price<100000):
        answer[0] = answer[0] + '구만'
        answer[1] = answer[1] + 'guman'
        price = price - 90000

    if(price == 100000):
        answer[0] = answer[0] + '십만'
        answer[1] = answer[1] + 'sibman'
        price = price - 100000

    if(999<price<2000):
        answer[0] = answer[0] + '천'
        answer[1] = answer[1] + 'cheon'
        price = price - 1000

    if(1999<price<3000):
        answer[0] = answer[0] + '이천'
        answer[1] = answer[1] + 'icheon'
        price = price - 2000

    if(2999<price<4000):
        answer[0] = answer[0] + '삼천'
        answer[1] = answer[1] + 'samcheon'
        price = price - 3000

    if(3999<price<5000):
        answer[0] = answer[0] + '사천'
        answer[1] = answer[1] + 'sacheon'
        price = price - 4000

    if(4999<price<6000):
        answer[0] = answer[0] + '오천'
        answer[1] = answer[1] + 'ocheon'
        price = price - 5000

    if(5999<price<7000):
        answer[0] = answer[0] + '육천'
        answer[1] = answer[1] + 'yukcheon'
        price = price - 6000

    if(6999<price<8000):
        answer[0] = answer[0] + '칠천'
        answer[1] = answer[1] + 'chilcheon'
        price = price - 7000

    if(7999<price<9000):
        answer[0] = answer[0] + '팔천'
        answer[1] = answer[1] + 'palcheon'
        price = price - 8000

    if(8999<price<10000):
        answer[0] = answer[0] + '구천'
        answer[1] = answer[1] + 'gucheon'
        price = price - 9000

    if(99<price<200):
        answer[0] = answer[0] + '백'
        answer[1] = answer[1] + 'baek'
        price = price - 100

    if(199<price<300):
        answer[0] = answer[0] + '이백'
        answer[1] = answer[1] + 'ibaek'
        price = price - 200

    if(299<price<400):
        answer[0] = answer[0] + '삼백'
        answer[1] = answer[1] + 'sambaek'
        price = price - 300

    if(399<price<500):
        answer[0] = answer[0] + '사백'
        answer[1] = answer[1] + 'sabaek'
        price = price - 400

    if(499<price<600):
        answer[0] = answer[0] + '오백'
        answer[1] = answer[1] + 'obaek'
        price = price - 500

    if(599<price<700):
        answer[0] = answer[0] + '육백'
        answer[1] = answer[1] + 'yukbaek'
        price = price - 600

    if(699<price<800):
        answer[0] = answer[0] + '칠백'
        answer[1] = answer[1] + 'chilbaek'
        price = price - 700

    if(799<price<900):
        answer[0] = answer[0] + '팔백'
        answer[1] = answer[1] + 'palbaek'
        price = price - 800

    if(899<price<1000):
        answer[0] = answer[0] + '구백'
        answer[1] = answer[1] + 'gubaek'
        price = price - 900

    if(9<price<20):
        answer[0] = answer[0] + '십'
        answer[1] = answer[1] + 'sib'
        price = price - 10

    if(19<price<30):
        answer[0] = answer[0] + '이십'
        answer[1] = answer[1] + 'isib'
        price = price - 20

    if(29<price<40):
        answer[0] = answer[0] + '삼십'
        answer[1] = answer[1] + 'samsib'
        price = price - 30

    if(39<price<50):
        answer[0] = answer[0] + '사십'
        answer[1] = answer[1] + 'sasib'
        price = price - 40

    if(49<price<60):
        answer[0] = answer[0] + '오십'
        answer[1] = answer[1] + 'osib'
        price = price - 50

    if(59<price<70):
        answer[0] = answer[0] + '육십'
        answer[1] = answer[1] + 'yuksib'
        price = price - 60

    if(69<price<80):
        answer[0] = answer[0] + '칠십'
        answer[1] = answer[1] + 'chilsib'
        price = price - 70

    if(79<price<90):
        answer[0] = answer[0] + '팔십'
        answer[1] = answer[1] + 'palsib'
        price = price - 80

    if(89<price<100):
        answer[0] = answer[0] + '구십'
        answer[1] = answer[1] + 'gusib'
        price = price - 90

    if(price==1):
        answer[0] = answer[0] + '일'
        answer[1] = answer[1] + 'il'

    if(price==2):
        answer[0] = answer[0] + '이'
        answer[1] = answer[1] + 'i'

    if(price==3):
        answer[0] = answer[0] + '삼'
        answer[1] = answer[1] + 'sam'

    if(price==4):
        answer[0] = answer[0] + '사'
        answer[1] = answer[1] + 'sa'

    if(price==5):
        answer[0] = answer[0] + '오'
        answer[1] = answer[1] + 'o'

    if(price==6):
        answer[0] = answer[0] + '육'
        answer[1] = answer[1] + 'yuk'

    if(price==7):
        answer[0] = answer[0] + '칠'
        answer[1] = answer[1] + 'chil'

    if(price==8):
        answer[0] = answer[0] + '팔'
        answer[1] = answer[1] + 'pal'

    if(price==9):
        answer[0] = answer[0] + '구'
        answer[1] = answer[1] + 'gu'

    return answer

def calculateQuantity(q):
        
    quantity = q
    answer = ['','']

    if(9<quantity<20):
        answer[0] = answer[0] + '열'
        answer[1] = answer[1] + 'yeol'
        quantity = quantity - 10

    if(19<quantity<30):
        answer[0] = answer[0] + '스무'
        answer[1] = answer[1] + 'seumu'
        quantity = quantity - 20

    if(29<quantity<40):
        answer[0] = answer[0] + '서른'
        answer[1] = answer[1] + 'seoreun'
        quantity = quantity - 30

    if(39<quantity<50):
        answer[0] = answer[0] + '마흔'
        answer[1] = answer[1] + 'maheun'
        quantity = quantity - 40

    if(49<quantity<60):
        answer[0] = answer[0] + '쉰'
        answer[1] = answer[1] + 'swin'
        quantity = quantity - 50

    if(59<quantity<70):
        answer[0] = answer[0] + '예순'
        answer[1] = answer[1] + 'yesun'
        quantity = quantity - 60

    if(69<quantity<80):
        answer[0] = answer[0] + '이흔'
        answer[1] = answer[1] + 'ilheun'
        quantity = quantity - 70

    if(79<quantity<90):
        answer[0] = answer[0] + '여든'
        answer[1] = answer[1] + 'yeodeun'
        quantity = quantity - 80

    if(89<quantity<100):
        answer[0] = answer[0] + '아흔'
        answer[1] = answer[1] + 'aheun'
        quantity = quantity - 90

    if(quantity==1):
        answer[0] = answer[0] + '한'
        answer[1] = answer[1] + 'han'

    if(quantity==2):
        answer[0] = answer[0] + '두'
        answer[1] = answer[1] + 'du'

    if(quantity==3):
        answer[0] = answer[0] + '세'
        answer[1] = answer[1] + 'se'

    if(quantity==4):
        answer[0] = answer[0] + '네'
        answer[1] = answer[1] + 'ne'

    if(quantity==5):
        answer[0] = answer[0] + '다섯'
        answer[1] = answer[1] + 'daseot'

    if(quantity==6):
        answer[0] = answer[0] + '여섯'
        answer[1] = answer[1] + 'yeoseot'

    if(quantity==7):
        answer[0] = answer[0] + '일곱'
        answer[1] = answer[1] + 'ilgob'

    if(quantity==8):
        answer[0] = answer[0] + '여덟'
        answer[1] = answer[1] + 'yeodeulb'

    if(quantity==9):
        answer[0] = answer[0] + '아홉'
        answer[1] = answer[1] + 'ahob'

    return answer

def calculateEachPhone(p):
    phone = str(p)
    answer = ['','']

    for x in range(len(phone)):
        if(phone[x]=='1'):
            answer[0] = answer[0] + '일'
            answer[1] = answer[1] + 'il'

        if(phone[x]=='2'):
            answer[0] = answer[0] + '이'
            answer[1] = answer[1] + 'i'
    
        if(phone[x]=='3'):
            answer[0] = answer[0] + '삼'
            answer[1] = answer[1] + 'sam'

        if(phone[x]=='4'):
            answer[0] = answer[0] + '사'
            answer[1] = answer[1] + 'sa'

        if(phone[x]=='5'):
            answer[0] = answer[0] + '오'
            answer[1] = answer[1] + 'o'

        if(phone[x]=='6'):
            answer[0] = answer[0] + '육'
            answer[1] = answer[1] + 'yuk'

        if(phone[x]=='7'):
            answer[0] = answer[0] + '칠'
            answer[1] = answer[1] + 'chil'

        if(phone[x]=='8'):
            answer[0] = answer[0] + '팔'
            answer[1] = answer[1] + 'pal'

        if(phone[x]=='9'):
            answer[0] = answer[0] + '구'
            answer[1] = answer[1] + 'gu'

        if(phone[x]=='0'):
            answer[0] = answer[0] + '공'
            answer[1] = answer[1] + 'gong'

    return answer

def calculatePhone(p1,p2,p3):

    phone = calculateEachPhone(p1)
    phone2 = calculateEachPhone(p2)
    phone3 = calculateEachPhone(p3)

    answer = [phone,phone2,phone3]

    return answer

def isVowel(char):
    found = False
    result = 0
    vowels1 = ['ㅏ','ㅗ']
    vowels2 = ['ㅓ','ㅜ','ㅣ','ㅔ','ㅐ','ㅡ','ㅠ','ㅛ','ㅑ','ㅕ','ㅒ','ㅖ','ㅟ','ㅚ']

    x = 0
    while (not found) and (x<len(vowels1)):
        if(char == vowels1[x]):
            result = 2
        x = x + 1
    x = 0
    while (not found) and (x<len(vowels2)):
        if(char == vowels2[x]):
            result = 1
        x = x + 1
    
    return result

def calculateVerb(root,manners,tense,negation):

    tenses = ['present','past','pastP','future','presentPro','pastPro','cannot']
    terminations = []

    answer = ['','','']

    root0=root[0]
    root1=root[1]
    root2=root[2]

    if(manners==0):
        _formality = 0
        _text = 'polite'
    else:
        _formality = 1
        _text = 'formal'

    # Present
    if(tenses[tense] == 'present'):
        # Polite
        if(_formality == 0):
                            # Consonant + V      Consonant + (아,오)      # 하다               # 이다
            terminations = [['어요','eoyo'],   ['아요','ayo'],      ['해요','haeyo'], ['이예요','iyeyo'],['예요','yeyo'],
                                    # Vocal                                                  # Vocal (아,오)
                        ['ㅕ','요','yeoyo'],['요','yo'],['ㅝ','요','woyo'],['ㅓ','요','eoyo'],['요','yo'],['ㅘ','요','wayo'],
                        ['ㅙ','요','waeyo']]
        
            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Exceptions
            if(root1[:-1].endswith('하'))or(root1[:-1].endswith('이')):
                # 하다
                if(root1[:-1].endswith('하')):
                    answer[1] = root1[:-2] + terminations[2][0]
                    answer[2] = root2[:-4] + terminations[2][1]
                # 이다
                if(root1[:-1].endswith('이')):
                    answer[1] = root1[:-2] + terminations[3][0]
                    answer[2] = root2[:-3] + terminations[3][1]                 
            else:
                root_syllables = jt.split_syllables(root1[:-1])
                # Ends in Consonant
                if(isVowel(root_syllables[len(root_syllables)-1])==0):
                    # Find last vowel
                    step = 1
                    while(isVowel(root_syllables[len(root_syllables)-step])==0):
                        step = step + 1
                    # Consonant + (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-step])==2):
                        answer[1] = root1[:-1] + terminations[1][0]
                        answer[2] = root2[:-2] + terminations[1][1]
                    else:
                        # Consonant + V
                        answer[1] = root1[:-1] + terminations[0][0]
                        answer[2] = root2[:-2] + terminations[0][1]
                else:
                    # Ends in Vowel
                    # Vocal (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-1])==2):
                        if(root_syllables[len(root_syllables)-1]=='ㅏ'):
                            answer[1] = root1[:-1] + terminations[9][0]
                            answer[2] = root2[:-2] + terminations[9][1]
                        if(root_syllables[len(root_syllables)-1]=='ㅗ'):
                            pool = root_syllables[:-1] + terminations[10][0]
                            answer[1] = jt.join_jamos(pool) + terminations[10][1]
                            answer[2] = root2[:-3] + terminations[10][2]                                                   
                    else:
                        # Vocal
                        if(root_syllables[len(root_syllables)-1]=='ㅣ'):
                            pool = root_syllables[:-1] + terminations[5][0]
                            answer[1] = jt.join_jamos(pool) + terminations[5][1]
                            answer[2] = root2[:-3] + terminations[5][2]  
                        if(root_syllables[len(root_syllables)-1]=='ㅓ')or(root_syllables[len(root_syllables)-1]=='ㅕ')or(root_syllables[len(root_syllables)-1]=='ㅐ'):
                            answer[1] = root1[:-1] + terminations[6][0]
                            answer[2] = root2[:-2] + terminations[6][1]
                        if(root_syllables[len(root_syllables)-1]=='ㅜ'):
                            pool = root_syllables[:-1] + terminations[7][0]
                            answer[1] = jt.join_jamos(pool) + terminations[7][1]
                            answer[2] = root2[:-3] + terminations[7][2]                      
                        if(root_syllables[len(root_syllables)-1]=='ㅡ'):
                            pool = root_syllables[:-1] + terminations[8][0]
                            answer[1] = jt.join_jamos(pool) + terminations[8][1]
                            answer[2] = root2[:-4] + terminations[8][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅔ')or(root_syllables[len(root_syllables)-1]=='ㅟ'):
                            answer[1] = root1[:-1] + terminations[0][0]
                            answer[2] = root2[:-2] + terminations[0][1]
                        if(root_syllables[len(root_syllables)-1]=='ㅚ'):
                            pool = root_syllables[:-1] + terminations[11][0]
                            answer[1] = jt.join_jamos(pool) + terminations[11][1]
                            answer[2] = root2[:-4] + terminations[11][2]
                      
        # Formal 
        if(_formality == 1):
                            # Consonant             # Vocal                 # 세다
            terminations = [['습니다','seubnida'],['ㅂ','니다','bnida'],['어봅니다','eobobnida']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            root_syllables = jt.split_syllables(root1[:-1])
            # Consonant
            if(isVowel(root_syllables[len(root_syllables)-1])==0):
                answer[1] = root1[:-1] + terminations[0][0]
                answer[2] = root2[:-2] + terminations[0][1]
            else:
                # Vocal
                if(root1=='세다'):
                    answer[1] = root1[:-1] + terminations[2][0]
                    answer[2] = root2[:-2] + terminations[2][1]  
                else:
                    pool = root_syllables + terminations[1][0]
                    answer[1] = jt.join_jamos(pool) + terminations[1][1]
                    answer[2] = root2[:-2] + terminations[1][2]

    # Past
    if(tenses[tense] == 'past'):
        # Polite
        if(_formality == 0):
                            # Consonant + V      Consonant + (아,오)                 # 하다                       # 이다
            terminations = [['었어요','eosseoyo'],    ['았어요','asseoyo'],    ['했어요','haesseoyo'], ['이었어요','ieosseoyo'],['였어요','yeosseoyo'],
                            # Vocal                                                                                         # Vocal (아,오)
                        ['ㅕㅆ','어요','yeosseoyo'],['ㅆ','어요','sseoyo'],['ㅝㅆ','어요','wosseoyo'],['ㅓㅆ','어요','eosseoyo'],['ㅆ','어요','sseoyo'],['ㅘㅆ','어요','wasseoyo'],
                          # 세다
                        ['어봤어요','eobwasseoyo']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Exceptions
            if(root1[:-1].endswith('하'))or(root1[:-1].endswith('이'))or(root1=='세다'):
                # 하다
                if(root1[:-1].endswith('하')):
                    answer[1] = root1[:-2] + terminations[2][0]
                    answer[2] = root2[:-4] + terminations[2][1]
                # 이다
                if(root1[:-1].endswith('이')):
                    answer[1] = root1[:-2] + terminations[3][0]
                    answer[2] = root2[:-3] + terminations[3][1]
                # 세다
                if(root1=='세다'):
                    answer[1] = root1[:-1] + terminations[11][0]
                    answer[2] = root2[:-2] + terminations[11][1]                 
            else:
                root_syllables = jt.split_syllables(root1[:-1])
                # Ends in Consonant
                if(isVowel(root_syllables[len(root_syllables)-1])==0):
                    # Find last vowel
                    step = 1
                    while(isVowel(root_syllables[len(root_syllables)-step])==0):
                        step = step + 1
                    # Consonant + (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-step])==2):
                        answer[1] = root1[:-1] + terminations[1][0]
                        answer[2] = root2[:-2] + terminations[1][1]
                    else:
                        # Consonant + V
                        answer[1] = root1[:-1] + terminations[0][0]
                        answer[2] = root2[:-2] + terminations[0][1]
                else:
                    # Ends in Vowel
                    # Vocal (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-1])==2):
                        if(root_syllables[len(root_syllables)-1]=='ㅏ'):
                            pool = root_syllables + terminations[9][0]
                            answer[1] = jt.join_jamos(pool) + terminations[9][1]
                            answer[2] = root2[:-2] + terminations[9][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅗ'):
                            pool = root_syllables[:-1] + terminations[10][0]
                            answer[1] = jt.join_jamos(pool) + terminations[10][1]
                            answer[2] = root2[:-3] + terminations[10][2]                                                   
                    else:
                        # Vocal
                        if(root_syllables[len(root_syllables)-1]=='ㅣ'):
                            pool = root_syllables[:-1] + terminations[5][0]
                            answer[1] = jt.join_jamos(pool) + terminations[5][1]
                            answer[2] = root2[:-3] + terminations[5][2]  
                        if(root_syllables[len(root_syllables)-1]=='ㅓ')or(root_syllables[len(root_syllables)-1]=='ㅕ')or(root_syllables[len(root_syllables)-1]=='ㅐ'):
                            pool = root_syllables + terminations[6][0]
                            answer[1] = jt.join_jamos(pool) + terminations[6][1]
                            answer[2] = root2[:-2] + terminations[6][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅜ'):
                            pool = root_syllables[:-1] + terminations[7][0]
                            answer[1] = jt.join_jamos(pool) + terminations[7][1]
                            answer[2] = root2[:-3] + terminations[7][2]                      
                        if(root_syllables[len(root_syllables)-1]=='ㅡ'):
                            pool = root_syllables[:-1] + terminations[8][0]
                            answer[1] = jt.join_jamos(pool) + terminations[8][1]
                            answer[2] = root2[:-4] + terminations[8][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅔ')or(root_syllables[len(root_syllables)-1]=='ㅟ')or(root_syllables[len(root_syllables)-1]=='ㅚ'):
                            pool = root_syllables + terminations[6][0]
                            answer[1] = jt.join_jamos(pool) + terminations[6][1]
                            answer[2] = root2[:-2] + terminations[6][2]

        # Formal 
        if(_formality == 1):
                            # Consonant + V                 Consonant + (아,오)        # Vocal (아,오)
            terminations = [['었습니다','eossseubnida'], ['았습니다','assseubnida'],    ['ㅆ','습니다','ssseubnida'],['ㅘㅆ','습니다','wassseubnida'],
                            # Vocal
                            ['ㅕㅆ','습니다','yeossseubnida'],['ㅆ','습니다','ssseubnida'],['ㅝㅆ','습니다','wossseubnida'],['ㅓㅆ','습니다','eossseubnida'],
                            # 하다                          # 이다
                            ['했습니다','haessseubnida'],['이었습니다','ieossseubnida'],['였습니다','yeossseubnida'],
                            # 세다
                            ['어봤습니다','eobwassseubnida']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Exceptions
            if(root1[:-1].endswith('하'))or(root1[:-1].endswith('이'))or(root1=='세다'):
                # 하다
                if(root1[:-1].endswith('하')):
                    answer[1] = root1[:-2] + terminations[8][0]
                    answer[2] = root2[:-4] + terminations[8][1]
                # 이다
                if(root1[:-1].endswith('이')):
                    answer[1] = root1[:-2] + terminations[9][0]
                    answer[2] = root2[:-3] + terminations[9][1]
                # 세다
                if(root1=='세다'):
                    answer[1] = root1[:-1] + terminations[11][0]
                    answer[2] = root2[:-2] + terminations[11][1]                  
            else:
                root_syllables = jt.split_syllables(root1[:-1])
                # Ends in Consonant
                if(isVowel(root_syllables[len(root_syllables)-1])==0):
                    # Find last vowel
                    step = 1
                    while(isVowel(root_syllables[len(root_syllables)-step])==0):
                        step = step + 1
                    # Consonant + (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-step])==2):
                        answer[1] = root1[:-1] + terminations[1][0]
                        answer[2] = root2[:-2] + terminations[1][1]
                    else:
                        # Consonant + V
                        answer[1] = root1[:-1] + terminations[0][0]
                        answer[2] = root2[:-2] + terminations[0][1]
                else:
                    # Ends in Vowel
                    # Vocal (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-1])==2):
                        if(root_syllables[len(root_syllables)-1]=='ㅏ'):
                            pool = root_syllables + terminations[2][0]
                            answer[1] = jt.join_jamos(pool) + terminations[2][1]
                            answer[2] = root2[:-2] + terminations[2][2] 
                        if(root_syllables[len(root_syllables)-1]=='ㅗ'):
                            pool = root_syllables[:-1] + terminations[3][0]
                            answer[1] = jt.join_jamos(pool) + terminations[3][1]
                            answer[2] = root2[:-3] + terminations[3][2]                                                   
                    else:
                        # Vocal
                        if(root_syllables[len(root_syllables)-1]=='ㅣ'):
                            pool = root_syllables[:-1] + terminations[4][0]
                            answer[1] = jt.join_jamos(pool) + terminations[4][1]
                            answer[2] = root2[:-3] + terminations[4][2]  
                        if(root_syllables[len(root_syllables)-1]=='ㅓ')or(root_syllables[len(root_syllables)-1]=='ㅕ')or(root_syllables[len(root_syllables)-1]=='ㅐ'):
                            pool = root_syllables + terminations[5][0]
                            answer[1] = jt.join_jamos(pool) + terminations[5][1]
                            answer[2] = root2[:-2] + terminations[5][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅜ'):
                            pool = root_syllables[:-1] + terminations[6][0]
                            answer[1] = jt.join_jamos(pool) + terminations[6][1]
                            answer[2] = root2[:-3] + terminations[6][2]                      
                        if(root_syllables[len(root_syllables)-1]=='ㅡ'):
                            pool = root_syllables[:-1] + terminations[7][0]
                            answer[1] = jt.join_jamos(pool) + terminations[7][1]
                            answer[2] = root2[:-4] + terminations[7][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅔ')or(root_syllables[len(root_syllables)-1]=='ㅟ')or(root_syllables[len(root_syllables)-1]=='ㅚ'):
                            pool = root_syllables + terminations[2][0]
                            answer[1] = jt.join_jamos(pool) + terminations[2][1]
                            answer[2] = root2[:-2] + terminations[2][2]

    # Past Perfect
    if(tenses[tense] == 'pastP'):
        # Polite
        if(_formality == 0):
                            # Consonant + V                 Consonant + (아,오)             # 하다                          # 이다
            terminations = [['었었어요','eosseosseoyo'],    ['았었어요','asseosseoyo'],    ['했었어요','haesseosseoyo'], ['이었었어요','ieosseosseoyo'],['였었어요','yeosseosseoyo'],
                            # Vocal                                                                                                                     # Vocal (아,오)                    
                        ['ㅕㅆ','었어요','yeosseosseoyo'],['ㅆ','었어요','sseosseoyo'],['ㅝㅆ','었어요','wosseosseoyo'],['ㅓㅆ','었어요','eosseosseoyo'],['ㅆ','었어요','sseosseoyo'],['ㅘㅆ','었어요','wasseosseoyo'],
                            # 세다
                        ['어봤었어요','eobwasseosseoyo']]
            
            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Exceptions
            if(root1[:-1].endswith('하'))or(root1[:-1].endswith('이'))or(root1=='세다'):
                # 하다
                if(root1[:-1].endswith('하')):
                    answer[1] = root1[:-2] + terminations[2][0]
                    answer[2] = root2[:-4] + terminations[2][1]
                # 이다
                if(root1[:-1].endswith('이')):
                    answer[1] = root1[:-2] + terminations[3][0]
                    answer[2] = root2[:-3] + terminations[3][1]
                # 세다
                if(root1=='세다'):
                    answer[1] = root1[:-1] + terminations[11][0]
                    answer[2] = root2[:-2] + terminations[11][1]                 
            else:
                root_syllables = jt.split_syllables(root1[:-1])
                # Ends in Consonant
                if(isVowel(root_syllables[len(root_syllables)-1])==0):
                    # Find last vowel
                    step = 1
                    while(isVowel(root_syllables[len(root_syllables)-step])==0):
                        step = step + 1
                    # Consonant + (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-step])==2):
                        answer[1] = root1[:-1] + terminations[1][0]
                        answer[2] = root2[:-2] + terminations[1][1]
                    else:
                        # Consonant + V
                        answer[1] = root1[:-1] + terminations[0][0]
                        answer[2] = root2[:-2] + terminations[0][1]
                else:
                    # Ends in Vowel
                    # Vocal (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-1])==2):
                        if(root_syllables[len(root_syllables)-1]=='ㅏ'):
                            pool = root_syllables + terminations[9][0]
                            answer[1] = jt.join_jamos(pool) + terminations[9][1]
                            answer[2] = root2[:-2] + terminations[9][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅗ'):
                            pool = root_syllables[:-1] + terminations[10][0]
                            answer[1] = jt.join_jamos(pool) + terminations[10][1]
                            answer[2] = root2[:-3] + terminations[10][2]                                                   
                    else:
                        # Vocal
                        if(root_syllables[len(root_syllables)-1]=='ㅣ'):
                            pool = root_syllables[:-1] + terminations[5][0]
                            answer[1] = jt.join_jamos(pool) + terminations[5][1]
                            answer[2] = root2[:-3] + terminations[5][2]  
                        if(root_syllables[len(root_syllables)-1]=='ㅓ')or(root_syllables[len(root_syllables)-1]=='ㅕ')or(root_syllables[len(root_syllables)-1]=='ㅐ'):
                            pool = root_syllables + terminations[6][0]
                            answer[1] = jt.join_jamos(pool) + terminations[6][1]
                            answer[2] = root2[:-2] + terminations[6][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅜ'):
                            pool = root_syllables[:-1] + terminations[7][0]
                            answer[1] = jt.join_jamos(pool) + terminations[7][1]
                            answer[2] = root2[:-3] + terminations[7][2]                      
                        if(root_syllables[len(root_syllables)-1]=='ㅡ'):
                            pool = root_syllables[:-1] + terminations[8][0]
                            answer[1] = jt.join_jamos(pool) + terminations[8][1]
                            answer[2] = root2[:-4] + terminations[8][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅔ')or(root_syllables[len(root_syllables)-1]=='ㅟ')or(root_syllables[len(root_syllables)-1]=='ㅚ'):
                            pool = root_syllables + terminations[6][0]
                            answer[1] = jt.join_jamos(pool) + terminations[6][1]
                            answer[2] = root2[:-2] + terminations[6][2]

        # Formal 
        if(_formality == 1):
                            # Consonant                          # Consonant (아,오)                 # Vocal (아,오)
            terminations = [['었었습니다','eosseossseubnida'], ['았었습니다','asseossseubnida'],    ['ㅆ','었습니다','sseossseubnida'],['ㅘㅆ','었습니다','wasseossseubnida'],
                            # Vocal
                            ['ㅕㅆ','었습니다','yeosseossseubnida'],['ㅆ','었습니다','sseossseubnida'],['ㅝㅆ','었습니다','wosseossseubnida'],['ㅓㅆ','었습니다','eosseossseubnida'],
                            # 하다                              # 이다
                            ['했었습니다','haesseossseubnida'],['이었었습니다','ieosseossseubnida'],['였었습니다','yeosseossseubnida'],
                            # 세다
                            ['어봤었습니다','eobwasseossseubnida']] 

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Exceptions
            if(root1[:-1].endswith('하'))or(root1[:-1].endswith('이'))or(root1=='세다'):
                # 하다
                if(root1[:-1].endswith('하')):
                    answer[1] = root1[:-2] + terminations[8][0]
                    answer[2] = root2[:-4] + terminations[8][1]
                # 이다
                if(root1[:-1].endswith('이')):
                    answer[1] = root1[:-2] + terminations[9][0]
                    answer[2] = root2[:-3] + terminations[9][1]
                # 세다
                if(root1=='세다'):
                    answer[1] = root1[:-1] + terminations[11][0]
                    answer[2] = root2[:-2] + terminations[11][1]                  
            else:
                root_syllables = jt.split_syllables(root1[:-1])
                # Ends in Consonant
                if(isVowel(root_syllables[len(root_syllables)-1])==0):
                    # Find last vowel
                    step = 1
                    while(isVowel(root_syllables[len(root_syllables)-step])==0):
                        step = step + 1
                    # Consonant + (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-step])==2):
                        answer[1] = root1[:-1] + terminations[1][0]
                        answer[2] = root2[:-2] + terminations[1][1]
                    else:
                        # Consonant + V
                        answer[1] = root1[:-1] + terminations[0][0]
                        answer[2] = root2[:-2] + terminations[0][1]
                else:
                    # Ends in Vowel
                    # Vocal (아,오)
                    if(isVowel(root_syllables[len(root_syllables)-1])==2):
                        if(root_syllables[len(root_syllables)-1]=='ㅏ'):
                            pool = root_syllables + terminations[2][0]
                            answer[1] = jt.join_jamos(pool) + terminations[2][1]
                            answer[2] = root2[:-2] + terminations[2][2] 
                        if(root_syllables[len(root_syllables)-1]=='ㅗ'):
                            pool = root_syllables[:-1] + terminations[3][0]
                            answer[1] = jt.join_jamos(pool) + terminations[3][1]
                            answer[2] = root2[:-3] + terminations[3][2]                                                   
                    else:
                        # Vocal
                        if(root_syllables[len(root_syllables)-1]=='ㅣ'):
                            pool = root_syllables[:-1] + terminations[4][0]
                            answer[1] = jt.join_jamos(pool) + terminations[4][1]
                            answer[2] = root2[:-3] + terminations[4][2]  
                        if(root_syllables[len(root_syllables)-1]=='ㅓ')or(root_syllables[len(root_syllables)-1]=='ㅕ')or(root_syllables[len(root_syllables)-1]=='ㅐ'):
                            pool = root_syllables + terminations[5][0]
                            answer[1] = jt.join_jamos(pool) + terminations[5][1]
                            answer[2] = root2[:-2] + terminations[5][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅜ'):
                            pool = root_syllables[:-1] + terminations[6][0]
                            answer[1] = jt.join_jamos(pool) + terminations[6][1]
                            answer[2] = root2[:-3] + terminations[6][2]                      
                        if(root_syllables[len(root_syllables)-1]=='ㅡ'):
                            pool = root_syllables[:-1] + terminations[7][0]
                            answer[1] = jt.join_jamos(pool) + terminations[7][1]
                            answer[2] = root2[:-4] + terminations[7][2]
                        if(root_syllables[len(root_syllables)-1]=='ㅔ')or(root_syllables[len(root_syllables)-1]=='ㅟ')or(root_syllables[len(root_syllables)-1]=='ㅚ'):
                            pool = root_syllables + terminations[2][0]
                            answer[1] = jt.join_jamos(pool) + terminations[2][1]
                            answer[2] = root2[:-2] + terminations[2][2]

    # Future
    if(tenses[tense] == 'future'):
        # Polite
        if(_formality == 0):
                            # Consonant                     # Vocal 
            terminations = [['을 거여요','eul geoyeoyo'],   ['ㄹ',' 거여요','l geoyeoyo']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            root_syllables = jt.split_syllables(root1[:-1])
            # Consonant
            if(isVowel(root_syllables[len(root_syllables)-1])==0):
                answer[1] = root1[:-1] + terminations[0][0]
                answer[2] = root2[:-2] + terminations[0][1]
            else:
                # Vocal
                pool = root_syllables + terminations[1][0]
                answer[1] = jt.join_jamos(pool) + terminations[1][1]
                answer[2] = root2[:-2] + terminations[1][2]

        # Formal 
        if(_formality == 1):
                            # Consonant       # Vocal
            terminations = [['을 거습니다','eul geoseubnida'],['ㄹ',' 거습니다','l geoseubnida'],
                            # 세다
                        ['어볼 거습니다','eobol geoseubnida']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Exceptions
            if(root1=='세다'):
                # 세다
                if(root1=='세다'):
                    answer[1] = root1[:-1] + terminations[2][0]
                    answer[2] = root2[:-2] + terminations[2][1]
            else:
                root_syllables = jt.split_syllables(root1[:-1])
                # Consonant
                if(isVowel(root_syllables[len(root_syllables)-1])==0):
                    answer[1] = root1[:-1] + terminations[0][0]
                    answer[2] = root2[:-2] + terminations[0][1]
                else:
                    # Vocal
                    pool = root_syllables + terminations[1][0]
                    answer[1] = jt.join_jamos(pool) + terminations[1][1]
                    answer[2] = root2[:-2] + terminations[1][2]

    # Present Progressive
    if(tenses[tense] == 'presentPro'):
        # Polite
        if(_formality == 0):
                            # Consonant/Vocal 
            terminations = [['고 있어요','go isseoyo']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Consonant/Vocal
            answer[1] = root1[:-1] + terminations[0][0]
            answer[2] = root2[:-2] + terminations[0][1]
    
        # Formal 
        if(_formality == 1):
                            # Consonant/Vocal
            terminations = [['고 있습니다','go issseubnida']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Consonant/Vocal
            answer[1] = root1[:-1] + terminations[0][0]
            answer[2] = root2[:-2] + terminations[0][1]

    # Past Progressive
    if(tenses[tense] == 'pastPro'):
        # Polite
        if(_formality == 0):
                            # Consonant/Vocal 
            terminations = [['고 있었어요','go isseosseoyo']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Consonant/Vocal
            answer[1] = root1[:-1] + terminations[0][0]
            answer[2] = root2[:-2] + terminations[0][1]
    
        # Formal 
        if(_formality == 1):
                            # Consonant/Vocal
            terminations = [['고 있었습니다','go isseossseubnida']]

            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

            # Consonant/Vocal
            answer[1] = root1[:-1] + terminations[0][0]
            answer[2] = root2[:-2] + terminations[0][1]

    # Cannot
    if(tenses[tense] == 'cannot'):
        # Adjectives cant use this tense, response would be empty
        if(root0.startswith('being')):
            answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text
            answer[1] = ''
            answer[2] = ''
        else:
            # Polite
            if(_formality == 0):
                                # Consonant/Vocal 
                terminations = [['지 못 해요','ji mos haeyo']]

                answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

                # Consonant/Vocal
                answer[1] = root1[:-1] + terminations[0][0]
                answer[2] = root2[:-2] + terminations[0][1]
        
            # Formal 
            if(_formality == 1):
                                # Consonant/Vocal
                terminations = [['지 못 합니다','ji mos habnida']]

                answer[0] = root0 + ' | ' + tenses[tense] + ' | ' + _text

                # Consonant/Vocal
                answer[1] = root1[:-1] + terminations[0][0]
                answer[2] = root2[:-2] + terminations[0][1]

    # 안 negation
    if(negation==1):
        answer[0] = 'not ' + answer[0]
        answer[1] = '안 ' + answer[1]
        answer[2] = 'an ' + answer[2]

    # 지 negation
    if(negation==2):
        term = calculateVerb(['do not','않다','anhda'],manners,tense,0)

        answer[0] = 'do not ' + root0 + ' | ' + tenses[tense] + ' | ' + _text
        answer[1] = root1[:-1] + '지 ' + term[1]
        answer[2] = root2[:-2] + 'ji ' + term[2]
 
    return answer