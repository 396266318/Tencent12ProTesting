# -*- coding: utf-8 -*-

import pytest

# def pytest_collection_modifyitems(session, config, items: list):
#     for item in items:
#         if "add" in item.nodeid:
#             item.add_marker(pytest.mark.add)
#         elif "sub" in item.nodeid:
#             item.add_marker(pytest.mark.sub)
#         elif "take" in item.nodeid:
#             item.add_marker(pytest.mark.take)
#         elif "div" in item.nodeid:
#             item.add_marker(pytest.mark.div)

    # items.reverse()   # 反向执行 在 testing 目录下执行 pytest -vs