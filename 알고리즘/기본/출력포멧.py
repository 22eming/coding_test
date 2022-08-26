#빈 자리는 빈공간으로 두고 , 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #빈자리로 두고, 오른쪽 정렬, 10자리

#양수일때는 + 표시 음수일때 -표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 , 찍어주기
print("{0:,}".format(100000000))
print("{0:+,}".format(10000000))

#3자리마다 콤마, 부호, 자리수 확보
print("{0:^<+30,}".format(1000000000))

#소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))