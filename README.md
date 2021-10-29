# Задача 1
Решение задачи 1 находится в файле [main.py](main.py). Минимальная версия python, необходимая для работы, это 
python 3.6 (click: >= 3.6, loguru >= 3.5, tqdm >= 2.7). Для корректной работы этого скрипта необходимо установить 
зависимости, находящиеся в файле [requirements.txt](requirements.txt) с помощью команды
```shell
pip instlal -r requirements.txt
```

Чтобы запустить данный скрипт нужно передать пути до лог файлов, которые необходимо смержить:
```shell
python main.py path/to/log_a.jsonl path/to/log_b.jsonl
```

Для отображения прогресса необходимо передать флаг `--verbose` или `-v`:
```shell
python main.py path/to/log_a.jsonl path/to/log_b.jsonl --verbose
```

Если необходимо выходной файл сохранить в определенное место, то можно воспользоваться ключом `--output` или `-o`:
```shell
python main.py path/to/log_a.jsonl path/to/log_b.jsonl --output path/to/output.jsonl
```

# Задача 2
Решение задачи 2 находится в файле [TASK2_SOLUTION.md](TASK2_SOLUTION.md)
