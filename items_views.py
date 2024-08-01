from fastapi import Path, APIRouter
from typing import Annotated

items_router = APIRouter(prefix='/items', tags=['items'])


@items_router.get('')
def items():
    return ['item1',
            'item2',
            'item3',
            ]


@items_router.get('/{item_id}/')
# значение item_id от 1 до 100
def get_item(item_id: Annotated[int, Path(ge=1, lt=100)]):
    return {'id': item_id}
