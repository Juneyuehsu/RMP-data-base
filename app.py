import streamlit as st
import pandas as pd
import os

# 使用相对路径读取Excel文件
file_path = os.path.join(os.path.dirname(__file__), 'ADP RMP collection.xlsx')
sheets = pd.read_excel(file_path, sheet_name=['GD_All', 'PD_All'])

# 选择数据表
df_gd_all = sheets['GD_All']
df_pd_all = sheets['PD_All']

# 将相关列转换为数值类型
columns_to_convert = ['Size', 'Brightness', 'ViewAngle_H', 'ViewAngle_V', 'Temp_L', 'Temp_H']
for col in columns_to_convert:
    df_gd_all[col] = pd.to_numeric(df_gd_all[col], errors='coerce')
    df_pd_all[col] = pd.to_numeric(df_pd_all[col], errors='coerce')

# 创建标题
st.title("Display Model Search_Beta")

# 选择数据来源
data_source = st.selectbox('Data Source', ['GD', 'PD'])

# 根据选择的数据来源确定要使用的数据表
if data_source == 'GD':
    df_all = df_gd_all
else:
    df_all = df_pd_all

# 创建下拉选单和输入框
size_options = [''] + sorted(df_all['Size'].dropna().unique().tolist())
resolution_options = [''] + sorted(df_all['Resolution_N'].dropna().unique().tolist())
interface_options = [''] + sorted(df_all['Interface'].dropna().unique().tolist())
temp_l_options = [''] + sorted(df_all['Temp_L'].dropna().unique().tolist())
temp_h_options = [''] + sorted(df_all['Temp_H'].dropna().unique().tolist())
brightness_options = [''] + sorted(df_all['Brightness'].dropna().unique().tolist())
view_angle_h_options = [''] + sorted(df_all['ViewAngle_H'].dropna().unique().tolist())
view_angle_v_options = [''] + sorted(df_all['ViewAngle_V'].dropna().unique().tolist())

size = st.selectbox('Size', size_options)
resolution = st.selectbox('Resolution', resolution_options)
brightness = st.selectbox('Brightness (leave blank if not needed)', brightness_options)
view_angle_h = st.selectbox('View Angle Horizontal (leave blank if not needed)', view_angle_h_options)
view_angle_v = st.selectbox('View Angle Vertical (leave blank if not needed)', view_angle_v_options)
interface = st.selectbox('Interface', interface_options)
temp_l = st.selectbox('LC Temperature Low (leave blank if not needed)', temp_l_options)
temp_h = st.selectbox('LC Temperature High (leave blank if not needed)', temp_h_options)

query = df_all
if size:
    query = query[query['Size'] == size]
if resolution:
    query = query[query['Resolution_N'] == resolution]
if brightness:
    query = query[query['Brightness'] >= int(brightness)]
if view_angle_h:
    query = query[query['ViewAngle_H'] >= int(view_angle_h)]
if view_angle_v:
    query = query[query['ViewAngle_V'] >= int(view_angle_v)]
if interface:
    query = query[query['Interface'] == interface]
if temp_l != '':
    query = query[query['Temp_L'] <= int(temp_l)]
if temp_h != '':
    query = query[query['Temp_H'] >= int(temp_h)]

st.write("The Models Matching：")
st.dataframe(query)

# 添加版权信息
st.write("")
st.write("Beta_rev-2, ACME internal only, by Alonso")