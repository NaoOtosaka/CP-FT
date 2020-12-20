import sys
import time

# 工作路径=======================================================================
# 主路径
work_path = sys.path[0]

# 项目创建路径
projectDir = work_path + '\\project\\'

# 模板文件路径
tempDir = work_path + '\\template\\'

# 模板文件设置====================================================================
# 完整用例模板
case_temp_file_name = 'caseTemplate.xlsx'

# 冒烟用例模板
smoke_case_temp_file_name = 'smokeTemplate.xlsx'

# H5兼容性模板
H5_compatibility_file_name = 'H5Compatibility.xlsx'

# WEB兼容性模板
web_compatibility_file_name = 'webCompatibility.xlsx'


# 自定义路径名====================================================================
# 项目名未输入时文件夹名称
default_project_name = time.strftime('%Y-%m-%d_%H-%M', time.localtime())

# 冒烟用例存放文件夹名称
smoke_dir_name = '冒烟测试'

# 原始用例存放文件夹名称
origin_case_dir_name = '原始用例'

# 执行用例存放文件夹名称
execute_case_dir_name = '执行用例'


# 自定义文件名====================================================================
# 完整用例模板导出后缀名
case_file_name = '-测试用例.xlsx'

# 冒烟用例模板导出后缀名
smoke_file_name = '-冒烟用例.xlsx'

# H5兼容性模板导出后缀名
H5_file_name = '-H5兼容性测试.xlsx'

# WEB兼容性模板导出后缀名
web_file_name = '-web兼容性测试.xlsx'

