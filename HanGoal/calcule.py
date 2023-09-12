#Dependencies



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
        price - 10000

    if(19999<price<30000):
        answer[0] = answer[0] + '이만'
        answer[1] = answer[1] + 'iman'
        price - 20000

    if(29999<price<40000):
        answer[0] = answer[0] + '삼만'
        answer[1] = answer[1] + 'samman'
        price - 30000

    if(39999<price<50000):
        answer[0] = answer[0] + '사만'
        answer[1] = answer[1] + 'saman'
        price - 40000

    if(49999<price<60000):
        answer[0] = answer[0] + '오만'
        answer[1] = answer[1] + 'oman'
        price - 50000

    if(59999<price<70000):
        answer[0] = answer[0] + '육만'
        answer[1] = answer[1] + 'yukman'
        price - 60000

    if(69999<price<80000):
        answer[0] = answer[0] + '칠만'
        answer[1] = answer[1] + 'chilman'
        price - 70000  

    if(79999<price<90000):
        answer[0] = answer[0] + '팔만'
        answer[1] = answer[1] + 'palman'
        price - 80000

    if(89999<price<100000):
        answer[0] = answer[0] + '구만'
        answer[1] = answer[1] + 'guman'
        price - 90000

    if(price == 100000):
        answer[0] = answer[0] + '십만'
        answer[1] = answer[1] + 'sibman'
        price - 100000

    if(999<price<2000):
        answer[0] = answer[0] + '천'
        answer[1] = answer[1] + 'cheon'
        price - 1000

    if(1999<price<3000):
        answer[0] = answer[0] + '이천'
        answer[1] = answer[1] + 'icheon'
        price - 2000

    if(2999<price<4000):
        answer[0] = answer[0] + '삼천'
        answer[1] = answer[1] + 'samcheon'
        price - 3000

    if(3999<price<5000):
        answer[0] = answer[0] + '사천'
        answer[1] = answer[1] + 'sacheon'
        price - 4000

    if(4999<price<6000):
        answer[0] = answer[0] + '오천'
        answer[1] = answer[1] + 'ocheon'
        price - 5000

    if(5999<price<7000):
        answer[0] = answer[0] + '육천'
        answer[1] = answer[1] + 'yukcheon'
        price - 6000

    if(6999<price<8000):
        answer[0] = answer[0] + '칠천'
        answer[1] = answer[1] + 'chilcheon'
        price - 7000

    if(7999<price<9000):
        answer[0] = answer[0] + '팔천'
        answer[1] = answer[1] + 'palcheon'
        price - 8000

    if(8999<price<10000):
        answer[0] = answer[0] + '구천'
        answer[1] = answer[1] + 'gucheon'
        price - 9000

    if(99<price<200):
        answer[0] = answer[0] + '천'
        answer[1] = answer[1] + 'baek'
        price - 100

    if(199<price<300):
        answer[0] = answer[0] + '이천'
        answer[1] = answer[1] + 'ibaek'
        price - 200

    if(299<price<400):
        answer[0] = answer[0] + '삼천'
        answer[1] = answer[1] + 'sambaek'
        price - 300

    if(399<price<500):
        answer[0] = answer[0] + '사천'
        answer[1] = answer[1] + 'sabaek'
        price - 400

    if(499<price<600):
        answer[0] = answer[0] + '오천'
        answer[1] = answer[1] + 'obaek'
        price - 500

    if(599<price<700):
        answer[0] = answer[0] + '육천'
        answer[1] = answer[1] + 'yukbaek'
        price - 600

    if(699<price<800):
        answer[0] = answer[0] + '칠천'
        answer[1] = answer[1] + 'chilbaek'
        price - 700

    if(799<price<900):
        answer[0] = answer[0] + '팔천'
        answer[1] = answer[1] + 'palbaek'
        price - 800

    if(899<price<1000):
        answer[0] = answer[0] + '구천'
        answer[1] = answer[1] + 'gubaek'
        price - 900

    if(9<price<20):
        answer[0] = answer[0] + '십'
        answer[1] = answer[1] + 'sib'
        price - 10

    if(19<price<30):
        answer[0] = answer[0] + '이십'
        answer[1] = answer[1] + 'isib'
        price - 20

    if(29<price<40):
        answer[0] = answer[0] + '삼십'
        answer[1] = answer[1] + 'samsib'
        price - 30

    if(39<price<50):
        answer[0] = answer[0] + '사십'
        answer[1] = answer[1] + 'sasib'
        price - 40

    if(49<price<60):
        answer[0] = answer[0] + '오십'
        answer[1] = answer[1] + 'osib'
        price - 50

    if(59<price<70):
        answer[0] = answer[0] + '육십'
        answer[1] = answer[1] + 'yuksib'
        price - 60

    if(69<price<80):
        answer[0] = answer[0] + '칠십'
        answer[1] = answer[1] + 'chilsib'
        price - 70

    if(79<price<90):
        answer[0] = answer[0] + '팔십'
        answer[1] = answer[1] + 'palsib'
        price - 80

    if(89<price<100):
        answer[0] = answer[0] + '구십'
        answer[1] = answer[1] + 'gusib'
        price - 90

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

def calculeQuantity(q):
        
    quantity = q
    answer = ['','']

    if(9<quantity<20):
        answer[0] = answer[0] + '열'
        answer[1] = answer[1] + 'yeol'
        quantity - 10

    if(19<quantity<30):
        answer[0] = answer[0] + '스무'
        answer[1] = answer[1] + 'seumu'
        quantity - 20

    if(29<quantity<40):
        answer[0] = answer[0] + '서른'
        answer[1] = answer[1] + 'seoreun'
        quantity - 30

    if(39<quantity<50):
        answer[0] = answer[0] + '마흔'
        answer[1] = answer[1] + 'maheun'
        quantity - 40

    if(49<quantity<60):
        answer[0] = answer[0] + '쉰'
        answer[1] = answer[1] + 'swin'
        quantity - 50

    if(59<quantity<70):
        answer[0] = answer[0] + '예순'
        answer[1] = answer[1] + 'yesun'
        quantity - 60

    if(69<quantity<80):
        answer[0] = answer[0] + '이흔'
        answer[1] = answer[1] + 'ilheun'
        quantity - 70

    if(79<quantity<90):
        answer[0] = answer[0] + '여든'
        answer[1] = answer[1] + 'yeodeun'
        quantity - 80

    if(89<quantity<100):
        answer[0] = answer[0] + '아흔'
        answer[1] = answer[1] + 'aheun'
        quantity - 90

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
        answer[0] = answer[0] + '이곱'
        answer[1] = answer[1] + 'ilgob'

    if(quantity==8):
        answer[0] = answer[0] + '여덟'
        answer[1] = answer[1] + 'yeodeulb'

    if(quantity==9):
        answer[0] = answer[0] + '아홉'
        answer[1] = answer[1] + 'ahob'

    return answer

def calculatePhone(pre,p1,p2):

    prefix = pre
    phone1 = p1
    phone2 = p2
    answer = [['',''],['',''],['','']]

    print("Doing")

    return answer