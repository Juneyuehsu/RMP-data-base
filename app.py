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

# 添加数据源列并合并数据表
df_gd_all['DataSource'] = 'GD'
df_pd_all['DataSource'] = 'PD'
df_all = pd.concat([df_gd_all, df_pd_all])

# 创建标题
st.title("Display Model Search_Beta")

# 选择数据来源
data_sources = st.multiselect('Data Source', ['GD', 'PD'])

# 如果没有选择数据源，则默认选择所有数据源
if not data_sources:
    data_sources = ['GD', 'PD']

# 根据选择的数据来源过滤数据表
if 'GD' in data_sources and 'PD' in data_sources:
    query = df_all
elif 'GD' in data_sources:
    query = df_all[df_all['DataSource'] == 'GD']
elif 'PD' in data_sources:
    query = df_all[df_all['DataSource'] == 'PD']
else:
    query = pd.DataFrame()  # 如果未选择任何数据源，则返回空数据框

# 创建下拉选单和输入框
size_options = [''] + sorted(query['Size'].dropna().unique().tolist())
resolution_options = [''] + sorted(query['Resolution_N'].dropna().unique().tolist())
interface_options = [''] + sorted(query['Interface'].dropna().unique().tolist())
temp_l_options = [''] + sorted(query['Temp_L'].dropna().unique().tolist())
temp_h_options = [''] + sorted(query['Temp_H'].dropna().unique().tolist())
brightness_options = [''] + sorted(query['Brightness'].dropna().unique().tolist())
view_angle_h_options = [''] + sorted(query['ViewAngle_H'].dropna().unique().tolist())
view_angle_v_options = [''] + sorted(query['ViewAngle_V'].dropna().unique().tolist())

size = st.selectbox('Size', size_options)
resolution = st.selectbox('Resolution', resolution_options)
brightness = st.selectbox('Brightness (leave blank if not needed)', brightness_options)
view_angle_h = st.selectbox('View Angle Horizontal (leave blank if not needed)', view_angle_h_options)
view_angle_v = st.selectbox('View Angle Vertical (leave blank if not needed)', view_angle_v_options)
interface = st.selectbox('Interface', interface_options)
temp_l = st.selectbox('LC Temperature Low (leave blank if not needed)', temp_l_options)
temp_h = st.selectbox('LC Temperature High (leave blank if not needed)', temp_h_options)

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

st.write("符合条件的型号如下：")
st.dataframe(query)

# 添加版权信息
st.write("")
st.write("Beta Rev-3rd by Alonso")
