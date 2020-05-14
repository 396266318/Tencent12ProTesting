# -*- coding: utf-8 -*-

import os
import pytest


if __name__ == "__main__":
    pytest.main(['-vs'])
    os.system(r"allure generate  --clean ./report -o ./html")
    os.system("allure open html")