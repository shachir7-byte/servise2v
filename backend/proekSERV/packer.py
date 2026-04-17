import os

# Список расширений, которые нам нужны
EXTENSIONS = ('.py', '.html', '.css', '.js')
# Папки, которые игнорируем (стандартные папки Django/Vue)
IGNORE_DIRS = ('.venv', 'node_modules', '__pycache__', '.git', 'migrations', 'static')

def pack_project(output_file='full_project_dump.txt'):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk('.'):
            # Игнорируем ненужные папки
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in files:
                if file.endswith(EXTENSIONS):
                    file_path = os.path.join(root, file)
                    outfile.write(f"\n{'='*20}\n")
                    outfile.write(f"FILE: {file_path}\n")
                    outfile.write(f"{'='*20}\n\n")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"Ошибка чтения: {e}")
                    
                    outfile.write("\n\n")
    print(f"Готово! Весь код собран в файл: {output_file}")

if __name__ == "__main__":
    pack_project()