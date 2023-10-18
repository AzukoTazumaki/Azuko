# from datetime import date
#
# date_test = [2023, 6, 30]
# print(date(date_test))
# from pathlib import Path
#
# p = Path('migrations')
# print([x for x in p.iterdir()])


# from datetime import time
#
# a = time.fromisoformat('00:02:24')
# print(a)

from fastapi.encoders import jsonable_encoder
from models.Data import albums

a = jsonable_encoder(albums)
print(a)