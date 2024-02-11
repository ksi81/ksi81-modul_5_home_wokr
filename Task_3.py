#3
import sys

def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу і повертає словник з розібраними компонентами.
    """
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """
    Завантажує логи з файлу та повертає список розібраних записів.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл логів не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує логи за рівнем логування.
    """
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість записів за рівнем логування.
    """
    counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    """
    Виводить результати підрахунку в читабельній формі.
    """
    print("Статистика за рівнями логування:")
    for level, count in counts.items():
        print(f"{level}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Введіть шлях до файлу логів.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
