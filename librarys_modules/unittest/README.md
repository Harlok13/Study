**Создание конфигурации для автоматического запуска тестов:**\
Edit configurations\
Unittests\
Custom\
Additional Arguments -> `discover -s <название папки с тестами> -p <*_test.py>`\
p.s. если тестовые файлы начинают с test, то в поиск нужно писать `<test_*.py>`
