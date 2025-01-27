# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChatRoleEnum(str, enum.Enum):
    SYSTEM = "SYSTEM"
    ASSISTANT = "ASSISTANT"
    USER = "USER"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatRoleEnum.SYSTEM:
            return system()
        if self is ChatRoleEnum.ASSISTANT:
            return assistant()
        if self is ChatRoleEnum.USER:
            return user()
