import pandas as pd

def main():
    df = pd.read_csv('上市公司資料.csv')
    df1 = df.dropna()
    df2 = df1.reindex(columns=['公司代號','出表日期','公司名稱','產業別','營業收入-當月營收','營業收入-上月營收'])
    df3 = df2.rename(columns={
        '營業收入-上月營收':'上月營收',
        '營業收入-當月營收':'當月營收'
        })
    df3.to_csv('上市公司資料整理.csv',encoding='utf-8')
    df3.to_excel('上市公司資料整理.xlsx')
    print("存檔完成")

if __name__ == '__main__':
    main()