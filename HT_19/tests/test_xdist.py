'''Створити 10 тестів, кожен з яких буде спочатку спати 2 секунди, потім assert True, або pass. Поставити на ці тести мітку "timed". 
Запустити тести так, щоб вони пройшли значно швидше ніж за 20 секунд. Команду запуску додати в текстовий файл в репозиторії домашки.'''

import pytest
import time


@pytest.mark.timed
def test_1():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_2():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_3():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_4():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_5():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_6():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_7():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_8():
    time.sleep(2)
    pass

@pytest.mark.timed
def test_9():
    time.sleep(2)
    pass
@pytest.mark.timed
def test_10():
    time.sleep(2)
    pass