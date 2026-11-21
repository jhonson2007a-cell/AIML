'''Date-21 Nov 2026
learning about numpy'''
import numpy as np
from pathlib import Path
# a=np.linspace(0.0,1.0,5)
# print(a)

# aa=np.zeros((4,5))
# print(aa)

# a=np.array([1,2,3,4,5,6,7,8,9,])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# b=a.reshape((3,3))
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)

# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# b=a.reshape((2,6))
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)

# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# b=a.reshape((5,3))
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)

# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# b=a.reshape((4,-1))
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)


# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# b=a.reshape((2,-1))
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)

# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# b=a.reshape((-1,3))
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)


# print(np.reshape(a.reshape(3, 4), (3, 4)))

# a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a)
# print(a.ndim,"\t",a.shape,"\t",a.dtype,"\t",a.size)
# print("\n")
# b=a.flatten()
# print(b)
# print(b.ndim,"\t",b.shape,"\t",b.dtype,"\t",b.size)


# seq=np.arange(12)
# grid=seq.reshape(3,4)
# auto_row=seq.reshape(-1,6)
# flat1=grid.ravel()
# flat2=grid.flatten()
# print(grid)
# print("auto_rows=",auto_row.shape)
# print(flat1)
# print(flat2)


# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.array([[100,200,300],[400,500,600],[700,800,900]])
# print(a)
# print("\n",b)
# print("\n",a+b)
# print("\n",a*b)
# print("\n",a@b)
# print("\n",np.add(a,b))
# print("\n",np.subtract(a,b))
# print("\n",np.multiply(a,b))
# print("\n",np.divide(a,b))
# print("\n",np.power(a,b))


# pri=np.array([250.0,400.0,1250.0,800.0])
# with_gst=pri*1.18
# disc=np.where(with_gst>1000,with_gst*0.90,with_gst)
# print("with_gst",with_gst)
# print("after discount=",disc)


# a=np.array([12,45,34,21,4,78,15,88])
# b=np.where(a>18,"\ncan vate\n","cannot vote")
# print(a)
# print(b)


# a=np.array([45,84,21,54,78,35,88])
# b=np.where(a>=48,"\npass\n","fail")
# print(a)
# print(b)


# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.array([[10,11,12]])
# print(a)
# print("\n",b)
# print("\n",a+b)

# a=np.array([[1,2,3],[4,5,6]])
# # b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) #give error becuase donot stretching 
# b=np.array([4,5,6])
# print(a)
# print("\n",b)
# print("\n",a+b)


# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b)
# c=b.T
# print(c)



'''learn abouts pandas'''
# import pandas as p
# mydic={"name":["abc","def","ghi"],"city":["x","y","z"]}
# print(type(mydic))
# print(mydic)
# df=p.DataFrame(mydic)
# print(type(df))
# print(df)


# mydic={"name":["jack","arman","imran","yuvraj","jhonson","owais","ayan"],
#        "city":["raipur","bhilai","sakti","raipur","raipur","mahasamund","champa"]}
# print(type(mydic))
# print(mydic)
# df=p.DataFrame(mydic)
# print(type(df))
# print(df)


# mydic={"name":["jack","arman","imran","yuvraj","jhonson","owais","ayan"],
#        "city":["raipur","bhilai","sakti","raipur","raipur","mahasamund","champa"]}
# print(type(mydic))
# print(mydic)
# df=p.DataFrame(mydic)
# print(type(df))
# print(df.sample(3))
# print(df.head()) 
# print(df.tail())                
# print(df.shape)                  
# print(df.columns)                
# print(df.describe())                          
# print(df.sort_values("city")) 

import pandas as pd
# df = pd.read_csv(Path(__file__).with_name("Iris.csv"))
print(df.info())