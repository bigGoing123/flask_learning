import numpy as np
height=[182,183,177,171,168,165,180,185,173]
weight=[73,68,70,61,67,63,80,75,73]
region=["Europe","Europe","Europe","Asia","Asia","Asia","America","America","America"]


def sort_and_map(num_array, str_array):
    # 对数值型数组进行排序，并记录排序后的索引
    sorted_indices = sorted(range(len(num_array)), key=lambda k: num_array[k])

    # 对数值型数组进行排序
    sorted_num_array = [num_array[i] for i in sorted_indices]

    # 对字符串数组按照排序后的索引进行调整
    sorted_str_array = [str_array[i] for i in sorted_indices]

    return sorted_num_array, sorted_str_array

def entropy(zi,mu):
    if zi==0:
        return 0
    return -zi/mu*np.log2(zi/mu)
def get_feature_gain(feature,region):
    feature1,region1=sort_and_map(feature,region)
    gain=[]
    for index,h in enumerate(feature1):
        #index+1在这里能记录region的数量
        if index>0 and feature1[index-1]==h:
            gain.pop() #把原来一样的数拿出来，需要更新
        E_num0,As_num0,Am_num0,E_num1,As_num1,Am_num1=0,0,0,0,0,0
        for i in range(len(region1)):
            if i<=index:
                if region1[i]=="Europe":
                    E_num0=E_num0+1
                elif region1[i]=="Asia":
                    As_num0=As_num0+1
                else:
                    Am_num0=Am_num0+1
            else :
                if region1[i]=="Europe":
                    E_num1=E_num1+1
                elif region1[i]=="Asia":
                    As_num1=As_num1+1
                else:
                    Am_num1=Am_num1+1
        Ent0=entropy(E_num0,index+1)+entropy(As_num0,index+1)+entropy(Am_num0,index+1)  #小于分界点的entropy计算
        len_r = len(region)-1-index#得到大于分界点之后的长度
        Ent1 = entropy(E_num1,len_r)+entropy(As_num1,len_r)+entropy(Am_num1,len_r) # 大于分界点的entropy计算
        now_gain=1.5850-((index+1)/len(region)*Ent0+len_r/len(region)*Ent1)
        gain.append(now_gain)
    return gain

if __name__ == '__main__':
    print("height",get_feature_gain(height,region))
    print("weight", get_feature_gain(weight, region))