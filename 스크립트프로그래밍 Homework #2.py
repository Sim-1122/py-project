#!/usr/bin/env python
# coding: utf-8

# ### 2020136078 심재규
# ### 스크립트프로그래밍 Homework #2
# ### [일반문제]
# ### 1. 다음 6 개의 Expression에 대해 Evaluation 결과 값을 출력하고, 해당 결과가 나온 이유에 대해 설명하시오
# - 1 and 2 and 3 and 4
# - 1 or 2 or 3 or 4
# - 1 and 2 or 3 and 4
# - (1 and 2) or (3 and 4)
# - 1 or 2 and 3 or 4
# - (1 or 2) and (3 or 4)

# In[1]:


1 and 2 and 3 and 4


# and 연산의 경우 마지막에 false가 오는지 확인해야 하기 때문에 4까지 확인 후 4를 리턴한다.

# In[2]:


1 or 2 or 3 or 4


# or 연산의 경우 앞에서 true가 올 경우 뒤를 보지 않고 1을 리턴한다.

# In[3]:


1 and 2 or 3 and 4


# and 연산자를 통해 2까지 확인한 후 or가 왔으므로 뒤를 확인하지 않고 2를 리턴한다.

# In[4]:


(1 and 2) or (3 and 4)


# 위와 같이 and 연산자를 통해 2까지 확인한 후 or가 왔으므로 뒤의 and를 확인하지 않고 2를 리턴한다.

# In[5]:


1 or 2 and 3 or 4


# 1 이후 or가 왔으므로 뒤를 확인하지 않고 1을 리턴한다.

# In[6]:


(1 or 2) and (3 or 4)


# or 연산을 통해 1과 3의 and 연산이므로 뒤에 있는 3을 리턴한다.

# ### 2. 경로에 해당하는 문자열 1개를 입력 받아 그 안에 디렉토리 경로명과 파일명을 분리하여 리스트로 반환하는 함수 div_path(s)를 작성하시오.
# - 인자로 전달하는 문자열은 경로만 들어간다고 가정한다.
# - 각 디렉토리와 파일을 구분하는 문자는 '/'로 가정한다.
# - 반환하는 리스트의 첫번째 원소는 디렉토리이고 두번째 원소는 파일명이다.
# - 다음과 같은 실행 및 출력 결과가 도출되어야 한다.
# - div_path('/usr/local/bin/python')
# * ['/usr/local/bin', 'python']
# - div_path('/home/chulsoo/test.txt')
# * ['/home/chulsoo', 'test.txt']
# - [참고] 리스트(l) 내에 새로운 정수값 (예를 들어 10)을 넣는 방법은 l.append(10) 이다.

# In[20]:


def div_path(s):
    number = 0
    c = ''
    for i in s.lstrip():
        number += 1
        if(i == '('):
            break
            
    s = s[number:]
    s = s.strip("')"); s = s.split('/')
    s = s[1:]
    
    str = []
    for i in range(len(s)-1):
        c = c + '/' + s[i]
    str.append(c)
    str.append(s[len(s)-1])
    return str

print ('문자열을 입력하시오: ')
s = input()
div_path(s)


# - div_path 함수는 입력한 문자열의 '('까지 문자열 왼쪽 끝을 잘라낸다.
# - 이후 문자열 슬라이싱을 하기 위해 리스트로 정의한다.
# - s.strip("')")을 통해 필요없는 오른쪽 문자열까지 잘라내고
# - 각 디렉토리와 파일을 구분하는 문자 '/'을 기점으로 분리해 리스트로 반환한다.
# - 이후 ' '가 생기므로 슬라이싱을 통해 자른다.
# - 각각의 원소를 append 메소드를 통해 더해주기 위해 새 리스트를 만든다.
# - 경로명까지 '/'를 사이에 더한 후 마지막 파일명은 ' '을 더한 후 더해준다.

# ### 3. 두 개의 리스트를 인자로 받아서 그 두 개의 리스트에 대한 '합집합'을 반환하는 함수 list_union(lista, listb)를 작성하시오.
# - 집합 자료형 set은 사용하지 않는다.
# - 인자로 전달하는 리스트 2 개에는 정수값만 들어간다고 가정하자.
# - 함수 내에서 새로운 리스트를 만들어 그 리스트 내에 인자로 받은 두 리스트의 모든 원소를 넣어 반환한다.
# - 반환하는 리스트에는 절대로 중복된 원소가 들어 있으면 안된다 (집합의 조건).
# - 반환하는 리스트는 정렬이 되어 있어야 한다.
# - 다음과 같은 실행 및 출력 결과가 도출되어야 한다.
# - list_union([1, 2, 3], [1, 2, 4])
# + [1, 2, 3, 4]
# - list_union([-10, -5, 0, -1], [100, 9, 0, 9])
# + [-10, -5, -1, 0, 9, 100]
# - list_union([0, 1, 2], [0, 1, 2])
# + [0, 1, 2]
# - [참고] 리스트(l) 내에 새로운 정수값 (예를 들어 10)을 넣는 방법은 l.append(10) 이다.
# - [참고] 임의의 정수값 (x)이 리스트 (l) 내에 존재하는지 판단하는 방법은 x in l 이다.

# In[25]:


def list_union(lista, listb):
    for i in listb:
        if(i not in lista):
            lista.append(i)
    return sorted(lista)

lista = [4,8,11]
listb = [1,2,4,11,19,18]
list_union(lista, listb)


# 두 리스트를 인자로 받아 lista에 없는 원소를 listb가 가지고 있다면 append 메소드를 통해 lista에 추가한 후 sorted를 통해 정렬한다.

# ### 4. 두 개의 리스트를 인자로 받아서 그 두 개의 리스트에 대한 '교집합'을 반환하는 함수 list_intersection(lista, listb)와 '차집합'을 반환하는 함수 list_difference(lista, listb)를 작성하시오.
# - 모든 가정과 조건은 3번 문제와 동일하다.

# In[29]:


def list_intersection(lista, listb):
    listc = []
    for i in listb:
        if(i in lista):
            listc.append(i)
    return sorted(listc)

lista = [4,8,11]
listb = [1,2,4,11,19,18]
list_intersection(lista, listb)


# 두 리스트를 인자로 받아 lista에 있는 원소를 listb가 가지고 있다면 append 메소드를 통해 새로 만든 listc에 추가한 후 sorted를 통해 정렬한다.

# In[31]:


def list_difference(lista, listb):
    for i in listb:
        if(i in lista):
            lista.remove(i)
    return sorted(lista)

lista = [4,8,11]
listb = [1,2,4,11,19,18]
list_difference(lista, listb)


# 두 리스트를 인자로 받아 lista에 있는 원소를 listb가 가지고 있다면 remove 메소드를 통해 공통된 원소를 빼고 sorted를 통해 정렬한다.

# ### 5. 두 개의 양의 정수를 인자로 받아서 해당 범위안에 있는 소수(prime number)의 리스트를 출력하는 함수 print_primenumber(a, b)를 작성하시오.
# - 이미 구현된 모듈이나 라이브러리는 사용하지 않는다.
# - 함수의 반환(return)은 없으며 함수 내의 끝에서 .format()을 사용하여 다음과 같이 출력한다.
# - print_primenumber(2, 10)
# - 2 이상 10 이하 정수 중 소수 리스트: [2, 3, 5, 7]

# In[41]:


def print_primenumber(a, b):
    def prime(n):
        if n<2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n%i == 0:
                    return False
            return True
    
    c = []
    for i in range(a, b):
        if prime(i):
            c.append(i)
    print("2 이상 10 이하 정수 중 소수 리스트: {list}".format(list=c))

print_primenumber(2, 10)


# 소수를 찾는 prime 함수를 정의한 후 a와 b범위 내에서 소수가 존재한다면 리스트 c에 append 메소드를 통해 추가하고
# .format()을 통해 출력해보는 작업을 한다.

# ### 소감
# 전체적인 난이도는 할만했습니다.
# 마지막 문제는 아직 해결하지 못해 시간 경과를 두고 다시 해봐야 할 것 같습니다.
