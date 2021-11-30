#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f_vector(n, v): 
    if n >= v:
        return "ERROR: rand_sphere: 2 <= dim < #vertices" 
    else:
        ar=[]
        e = 0
        f = 0
        if n==2:
            ar.append(v)
            e += v
            ar.append(e)
            return ar
        elif n==3:
            ar.append(v)
            if v==4:
                e += 2*v-2
                f += v
                ar.append(e)
                ar.append(f)
                return ar
            elif v > 4:
                e += 3*v-6
                f += 2*v-4
                ar.append(e)
                ar.append(f)
                return ar
        elif n==4:
            mx = []
            ver=0
            x=0
            ar.append(v)
            for _ in range(0,n):
                mx.append([])
            for i in range(1,v+1):
                ver+=i
                mx[0].append(i)

            for j in range(1,v+1):
                if j<=1:
                    mx[1].append(0)
                else:
                    e+=mx[0][j-2]
                    mx[1].append(e)
            ar.append(e)
            
            for k in range(1,v+1):
                if k<=2:
                    mx [2].append(0)
                else:
                    f+=mx[1][k-2]
                    mx[2].append(f)
            ar.append(f)
            
            for l in range(1,v+1):
                if l<=3:
                    mx[3].append(0)
                else:
                    x+=mx[2][l-2]
                    mx[3].append(x)
            ar.append(x)
            
            return ar


# In[2]:


def f_vector2(n, v):
    if n >= v:
        return "ERROR: rand_sphere: 2 <= dim < #vertices"
    else:
        ar=[]
        e = 0
        f = 0
        if n==2:
            ar.append(v)
            e += v
            ar.append(e)
            return ar
        elif n==3:
            ar.append(v)
            if v==4:
                e += 2*v-2
                f += v
                ar.append(e)
                ar.append(f)
                return ar
            elif v > 4:
                e += 3*v-6
                f += 2*v-4
                ar.append(e)
                ar.append(f)
                return ar
        else:
            sum_e = 0
            sum_f = 0
            last = 0
            # vertex
            f_v = f_vector2(n-1, n)[0] + v-n
            ar.append(f_v)
            #edege
            for i in range(n,v):
                sum_e+=i
            f_e = f_vector2(n-1, n)[1] + sum_e
            ar.append(f_e)
            # 면부터 다포체
            for i in range(2,n-1):
                if (v-n == 1):
                    x=0
                    x=f_vector2(n-1,n)[i-1]+f_vector2(n-1,n)[i]
                    ar.insert(i,x)
                elif (v-n >= 2):
                    y=0
                    y=f_vector2(n,v-1)[i-1]+f_vector2(n,v-1)[i]
                    ar.insert(i,y)
            # 마지막 수, 오일러 함수 이용 
            if n%2 == 0:
                for i in range(0,n-1):
                    last += ar[i]*(-1) **i
                ar.append(last)
            else:
                for i in range(0,n-1):
                    last += ar[i]*(-1)** i
                last = 2 - last
                ar.append(last)
            return ar


# In[3]:


def pyramid(n,v):
    rs = []
    ar = f_vector(n, v)
    i=0
    if n==2:
        rs.append(ar[0]+1)
        rs.append(ar[1]+ar[0])
        rs.append(1+ar[1])
    else:
        rs.append(ar[0]+1)
        for i in range(1, n):
            rs.append(ar[i]+ar[i-1])
        rs.append(1+ar[n-1])
    return rs


# In[4]:


def pyramid2(n,v):
    rs = []
    ar = f_vector2(n, v)
    i=0
    if n==2:
        rs.append(ar[0]+1)
        rs.append(ar[1]+ar[0])
        rs.append(1+ar[1])
    else:
        rs.append(ar[0]+1)
        for i in range(1, n):
            rs.append(ar[i]+ar[i-1])
        rs.append(1+ar[n-1])
    return rs


# In[5]:


def prism(n, v):
    rs = []
    ar = f_vector(n, v)
    i =0
    if n==2:
        rs.append(2*ar[0])
        rs.append(2*ar[1]+ar[0])
        rs.append(2+ar[1])
    else:
        rs.append(2*ar[0])
        for i in range(1, n):
            rs.append(2*ar[i]+ar[i-1])
        rs.append(2+ar[n-1])
    return rs


# In[6]:


def prism2(n, v):
    rs = []
    ar = f_vector2(n, v)
    i =0
    if n==2:
        rs.append(2*ar[0])
        rs.append(2*ar[1]+ar[0])
        rs.append(2+ar[1])
    else:
        rs.append(2*ar[0])
        for i in range(1, n):
            rs.append(2*ar[i]+ar[i-1])
        rs.append(2+ar[n-1])
    return rs


# In[7]:


f_vector(3,12)


# In[8]:


f_vector(3,12)


# In[9]:


pyramid(3,12)


# In[10]:


prism(3,12)


# In[11]:


f_vector2(8,9)


# In[12]:


pyramid2(8,9)


# In[ ]:




