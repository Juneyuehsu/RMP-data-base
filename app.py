import streamlit as st
import pandas as pd
import os

# 使用相对路径读取Excel文件
file_path = os.path.join(os.path.dirname(__file__), 'ADP RMP collection.xlsx')
sheets = pd.read_excel(file_path, sheet_name=['GD_All', 'PD_All'])

# 选择数据表
df_gd_all = sheets['GD_All']
df_pd_all = sheets['PD_All']

# 创建标题
st.title("Display Model Search")

# 创建下拉选单和输入框
size_options = [''] + sorted(df_gd_all['Size'].dropna().unique().tolist())
resolution_options = [''] + sorted(df_gd_all['Resolution_N'].dropna().unique().tolist())
interface_options = [''] + sorted(df_gd_all['Interface'].dropna().unique().tolist())
temp_l_options = [''] + sorted(df_gd_all['Temp_L'].dropna().unique().tolist())
temp_h_options = [''] + sorted(df_gd_all['Temp_H'].dropna().unique().tolist())
brightness_options = [''] + sorted(df_gd_all['Brightness'].dropna().unique().tolist())
view_angle_h_options = [''] + sorted(df_gd_all['ViewAngle_H'].dropna().unique().tolist())
view_angle_v_options = [''] + sorted(df_gd_all['ViewAngle_V'].dropna().unique().tolist())

size = st.selectbox('Size', size_options, key='size')
resolution = st.selectbox('Resolution', resolution_options, key='resolution')
brightness = st.selectbox('Brightness (leave blank if not needed)', brightness_options, key='brightness')
view_angle_h = st.selectbox('View Angle Horizontal (leave blank if not needed)', view_angle_h_options, key='view_angle_h')
view_angle_v = st.selectbox('View Angle Vertical (leave blank if not needed)', view_angle_v_options, key='view_angle_v')
interface = st.selectbox('Interface', interface_options, key='interface')
temp_l = st.selectbox('LC Temperature Low (leave blank if not needed)', temp_l_options, key='temp_l')
temp_h = st.selectbox('LC Temperature High (leave blank if not needed)', temp_h_options, key='temp_h')

# 根据用户输入进行数据筛选
query = df_gd_all
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

# 显示筛选结果
st.write("符合条件的型号如下：")
st.dataframe(query[['Model Name', 'Resolution_N', 'Size', 'Brightness', 'ViewAngle_H', 'ViewAngle_V', 'Interface', 'Panel Type', 'PPI', 'Temp_L', 'Temp_H', 'LED Life', 'Color Bit', 'LED Driver', 'Color', 'Note', 'Status']])
