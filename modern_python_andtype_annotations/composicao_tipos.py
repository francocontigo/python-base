from typing import Union, List, Any, Optional

# def soma(a: Union[int, str], b: Union[int, str]):
#     return a + b

# soma(1, 2)
# soma("Ricardo", "Franco")

OptionalMessege = Optional[Union[str, int, List]]

def imprime_mensagem(msg: int | str | list | float | None = None) -> None:
    print(msg)

# def imprime_mensagem(msg: OptionalMessege = None):
#     print(msg)


# def imprime_mensagem(msg: Optional[Union[str, int, List]] = None):
#     print(msg)


# def imprime_mensagem(msg: Any):
#     print(msg)

# def imprime_mensagem(msg: Union[str, int, List]):
#     print(msg) # Printable __str__


imprime_mensagem("Ricardo")
imprime_mensagem(123)
imprime_mensagem([1, 2, 3])
