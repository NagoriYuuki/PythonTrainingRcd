import pandas as pd

# 1. 读取数据
file_path = "clist.csv"  # 替换为你的文件名
df = pd.read_csv(file_path)

# 2. 复制 DataFrame 避免污染
df_clean = df.copy()

# 3. 清洗 problem-luck-column 百分比为 float
df_clean['pass_rate'] = df_clean['problem-luck-column'].str.rstrip('%').astype(float)

# 4. 整合标签列为 list
tag_cols = ['tag', 'tag 2', 'tag 3', 'tag 4', 'tag 5']
df_clean['tags'] = df_clean[tag_cols].values.tolist()
df_clean['tags'] = df_clean['tags'].apply(lambda x: [tag for tag in x if pd.notnull(tag)])

# 5. 重命名 coder-color 列为 rating_or_passnum
df_clean.rename(columns={'coder-color': 'rating_or_passnum'}, inplace=True)

# 6. 生成最终 DataFrame
df_final = df_clean[['problem-date-column', 'nowrap', 'rating_or_passnum', 'pass_rate', 'tags']].copy()
df_final.columns = ['date', 'title', 'rating_or_passnum', 'pass_rate', 'tags']

# 7. 保存为 csv（utf-8 编码，index 不导出）
output_path = "cf_cleaned.csv"
df_final.to_csv(output_path, index=False, encoding='utf-8-sig')

print("✅ 数据清洗完成，已保存为 cf_cleaned.csv")
