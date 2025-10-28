import pandas as pd
#设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

def get_dataframe_from_excel():
    #pd.read_excel()函数用于读取Excel文件的数据
    #'supermarket_sales.xlsx'表示Excel文件的路径及名称
    #sheet_name='销售数据'表示读取名为“销售数据”的工作表的数据
    #skiprows=1表示跳过Excel中的第一行，因为第一行是标题
    #index_col='订单号’表示将订单号这一列作为返回的数据框的索引

    df = pd.read_excel('supermarket_sales.xlsx',
                        sheet_name ='销售数据',
                        skiprows =1,
                        index_col='订单号'
                        )
    #df['时间'取出原有的'时间'这一列，其中包含交易的完整的时间字符串，如'10:25:30'
    #pd.to_datetime将'时间'列转化成datetime类型
    #format ="%H:%M:%S"指定了原有时间字符串的格式
    #dt.hour表示从转化后的数据框取出小时数作为新列
    #最后赋值给sale_df['小时数'],这样就得到了一个包含交易小时的新列
    df['小时数'] = pd.to_datetime(df["时间"], format ="%H:%M:%S").dt.hour
    return df

sale_df = get_dataframe_from_excel()

print("销售数据的前5行如下:")
print(sale_df.head())

print("销售数据各列的详细信息如下:")
sale_df.info()
