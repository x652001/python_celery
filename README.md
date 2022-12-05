
## File

~~~
.
├── compile.sh 
├── requirements.txt
├── pyinstaller_hooks_folder  
│   └── hook-celery.py        -> for pyinstaller compile celery
├── web.py                    -> 模擬Web對Task操作
├── worker.py                 -> 開啟Celery Instance
└── workers                   -> 用來放所有Celery Task
    ├── __init__.py
    ├── worker_add.py         -> Celery其中一個Task
    └── worker_main.py        -> Celery主要Instance
~~~

## Require

- Redis


## 開啟Celery

```shell
python3 worker.py
```


## 新增Queue

```shell
python3 web.py
```

