import sys
import time
import os
from tools.setConfig import load_conf

conf = load_conf()

# 工作路径=======================================================================
# 主路径
# work_path = os.path.dirname(os.path.realpath(sys.executable))

# 项目创建路径
projectDir = conf['projectDir']

# 模板文件路径
tempDir = conf['tempDir']

# 模板文件设置====================================================================
# 完整用例模板
case_temp_file_name = conf['case_temp_file_name']

# 冒烟用例模板
smoke_case_temp_file_name = conf['smoke_case_temp_file_name']

# H5兼容性模板
H5_compatibility_file_name = conf['H5_compatibility_file_name']

# WEB兼容性模板
web_compatibility_file_name = conf['web_compatibility_file_name']


# 自定义路径名====================================================================
# 项目名未输入时文件夹名称
default_project_name = time.strftime('%Y-%m-%d_%H-%M', time.localtime())

# 冒烟用例存放文件夹名称
smoke_dir_name = conf['smoke_dir_name']

# 原始用例存放文件夹名称
origin_case_dir_name = conf['origin_case_dir_name']

# 执行用例存放文件夹名称
execute_case_dir_name = conf['execute_case_dir_name']


# 自定义文件名====================================================================
# 完整用例模板导出后缀名
case_file_name = conf['case_file_name']

# 冒烟用例模板导出后缀名
smoke_file_name = conf['smoke_file_name']

# H5兼容性模板导出后缀名
H5_file_name = conf['H5_file_name']

# WEB兼容性模板导出后缀名
web_file_name = conf['web_file_name']

