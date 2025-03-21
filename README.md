To get wrongly-abbreviated type annotations:
```
pip install -r requirements.lock
mkdocs serve
```

They are displayed in the built documentation as:
```
mylib.some_fn(tuple_arg: tuple, union_arg: Union, modern_union_arg_this_one_works: int | str, unless_it_has_a_literal: Union)
```
