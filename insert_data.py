import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import engine, GD_All

# 使用本地文件路徑
file_path = 'C:/Users/alonsohsu/OneDrive - 進金生實業股份有限公司/Desktop/My work/Python/RMP data base/ADP RMP collection.xlsx'
sheets = pd.read_excel(file_path, sheet_name=['GD_All'])

# 創建數據庫會話
Session = sessionmaker(bind=engine)
session = Session()

# 將數據插入數據庫
for _, row in sheets['GD_All'].iterrows():
    gd_all = GD_All(
        resolution_n=row['Resolution_N'],
        resolution_x=row['Resolution_X'],
        resolution_y=row['Resolution_Y'],
        size=row['Size'],
        aspect_ratio=row['Aspect Ratio'],
        panel_type=row['Panel Type'],
        ppi=row['PPI'],
        model_name=row['Model Name'],
        brightness=row['Brightness'],
        viewangle_h=row['ViewAngle_H'],
        viewangle_v=row['ViewAngle_V'],
        temp_l=row['Temp_L'],
        temp_h=row['Temp_H'],
        led_life=row['LED Life'],
        color_bit=row['Color Bit'],
        led_driver=row['LED Driver'],
        interface=row['Interface'],
        color=row['Color'],
        note=row['Note'],
        status=row['Status']
    )
    session.add(gd_all)
session.commit()
