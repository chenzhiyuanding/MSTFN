#把连续4个的其他action换成2，FP
import os
import re

def extract_number(file_name):
    """从文件名中提取最后的数字"""
    match = re.search(r'(\d+)\.txt$', file_name)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"文件名格式不正确: {file_name}")

def modify_file_content(file_path, action_num):
    """将txt文件的最后一列改为3"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # 修改每一行的最后一列
    modified_lines = []
    for line in lines:
        parts = line.split()
        if len(parts) > 0:
            parts[-1] = str(action_num)
            modified_lines.append(' '.join(parts) + '\n')
        else:
            modified_lines.append(line)
    
    # 写回文件
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def process_files(file_list, action_num):
    """处理文件列表，找到符合条件的文件并修改其内容"""
    if not file_list:
        return

    # 提取所有文件名中的数字
    # number_to_file = {extract_number(f): f for f in file_list}
    # sorted_numbers = number_to_file
    num_list = [extract_number(f) for f in file_list]
    consecutive_groups = []
    temp_group = []
    temp_index_group = []
    for i in range(len(num_list)):
        if not temp_group or (num_list[i] - temp_group[-1]) == 5:
            temp_group.append(num_list[i])
            temp_index_group.append(i)
        else:
            if len(temp_group) >= 4:
                consecutive_groups.append(temp_index_group)
            temp_group = [num_list[i]]
            temp_index_group = [i]
    
    # 检查最后一个临时组
    if len(temp_group) >= 4:
        consecutive_groups.append(temp_index_group)

    # 获取符合条件的文件路径
    files_to_modify = []
    for group in consecutive_groups:
        files_to_modify.extend([file_list[num] for num in group])

    # 修改文件内容
    for file_path in set(files_to_modify):  # 使用set去重
        modify_file_content(file_path, action_num)
