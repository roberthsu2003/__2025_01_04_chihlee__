import pandas as pd

def main():
    """
    主函數，用於讀取CSV文件，進行數據清洗和轉換，並將結果保存為CSV和Excel文件。
    """
    # 讀取名為'上市公司資料.csv'的CSV文件，並將數據存儲在DataFrame對象df中。
    try:
        df = pd.read_csv('上市公司資料.csv')
    except FileNotFoundError:
        print("Error: 上市公司資料.csv not found.")
        return
    
    # 移除df中包含任何NaN（缺失值）的行，並將結果存儲在新的DataFrame對象df1中。
    df1 = df.dropna()
    
    # 重新索引df1的列，只保留指定的列，並將結果存儲在新的DataFrame對象df2中。
    # 保留的列包括：'公司代號'、'出表日期'、'公司名稱'、'產業別'、'營業收入-當月營收'、'營業收入-上月營收'。
    df2 = df1.reindex(columns=['公司代號','出表日期','公司名稱','產業別','營業收入-當月營收','營業收入-上月營收'])
    
    # 重命名df2中的列名，將'營業收入-上月營收'改為'上月營收'，將'營業收入-當月營收'改為'當月營收'，並將結果存儲在新的DataFrame對象df3中。
    df3 = df2.rename(columns={
        '營業收入-上月營收':'上月營收',
        '營業收入-當月營收':'當月營收'
        })
    
    # 將df3的數據保存到名為'上市公司資料整理.csv'的CSV文件中，並使用utf-8編碼。
    df3.to_csv('上市公司資料整理.csv',encoding='utf-8', index=False)
    
    # 將df3的數據保存到名為'上市公司資料整理.xlsx'的Excel文件中。
    # 修正: to_excel() 不支援 encoding 參數
    df3.to_excel('上市公司資料整理.xlsx', index=False)
    
    # 印出"存檔完成"的字串，表示檔案儲存完成。
    print("存檔完成")

# 檢查是否直接執行此腳本。如果是，則執行main()函數。
if __name__ == '__main__':
    main()
