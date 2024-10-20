import shutil
from pathlib import Path
import logging
import os

log_filename = '../logs/backup.log'
logging.basicConfig(filename=log_filename,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def copy_files_with_logging(source_dir: str, target_dir: str):

    try:
        # Проверяем существование исходной директории
        if not Path(source_dir).exists():
            raise FileNotFoundError(f"Исходная директория не найдена: {source_dir}")

        # Создаем целевую директорию, если она не существует
        Path(target_dir).mkdir(parents=True, exist_ok=True)

        # Копируем все файлы
        for file in Path(source_dir).iterdir():
            if file.is_file():
                try:
                    shutil.copy(file, target_dir)
                    logging.info(f'Файл {file.name} успешно скопирован в {target_dir}')
                except Exception as e:
                    logging.error(f'Ошибка при копировании файла {file.name}: {e}')
            else:
                logging.warning(f'{file.name} не является файлом и пропущен')
    except Exception as e:
        logging.critical(f'Ошибка при выполнении резервного копирования: {e}')


def main():

    source = str(input('Source directory '))
    target = str(input('Backup directory '))

    logging.info('Запуск процесса резервного копирования')
    copy_files_with_logging(source, target)
    logging.info('Процесс завершен')


if __name__ == "__main__":
    main()
