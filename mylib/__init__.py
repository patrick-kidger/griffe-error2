from typing import Literal, Union

def some_fn(
    tuple_arg: tuple[int, str],
    union_arg: Union[int, str],
    modern_union_arg_this_one_works: int | str,
    unless_it_has_a_literal: int | Literal[1]
):
    pass
