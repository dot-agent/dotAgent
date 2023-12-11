"""Stub file for nextpy/components/chakra/overlay/tooltip.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from nextpy.backend.vars import Var, BaseVar, ComputedVar
from nextpy.backend.event import EventChain, EventHandler, EventSpec
from nextpy.frontend.style import Style
from typing import Any, Union
from nextpy.frontend.components.chakra import ChakraComponent, LiteralChakraDirection
from nextpy.backend.vars import Var

class Tooltip(ChakraComponent):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        arrow_padding: Optional[Union[Var[int], int]] = None,
        arrow_shadow_color: Optional[Union[Var[str], str]] = None,
        arrow_size: Optional[Union[Var[int], int]] = None,
        delay: Optional[Union[Var[int], int]] = None,
        close_on_click: Optional[Union[Var[bool], bool]] = None,
        close_on_esc: Optional[Union[Var[bool], bool]] = None,
        close_on_mouse_down: Optional[Union[Var[bool], bool]] = None,
        default_is_open: Optional[Union[Var[bool], bool]] = None,
        direction: Optional[
            Union[Var[Literal["ltr", "rtl"]], Literal["ltr", "rtl"]]
        ] = None,
        gutter: Optional[Union[Var[int], int]] = None,
        has_arrow: Optional[Union[Var[bool], bool]] = None,
        is_disabled: Optional[Union[Var[bool], bool]] = None,
        is_open: Optional[Union[Var[bool], bool]] = None,
        label: Optional[Union[Var[str], str]] = None,
        open_delay: Optional[Union[Var[int], int]] = None,
        placement: Optional[Union[Var[str], str]] = None,
        should_wrap_children: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_close: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_open: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Tooltip":
        """Create the component.

        Args:
            *children: The children of the component.
            arrow_padding: The padding required to prevent the arrow from reaching the very edge of the popper.
            arrow_shadow_color: The color of the arrow shadow.
            arrow_size: Size of the arrow.
            delay: Delay (in ms) before hiding the tooltip
            close_on_click: If true, the tooltip will hide on click
            close_on_esc: If true, the tooltip will hide on pressing Esc key
            close_on_mouse_down: If true, the tooltip will hide while the mouse is down
            default_is_open: If true, the tooltip will be initially shown
            direction: Theme direction ltr or rtl. Popper's placement will be set accordingly
            gutter: The distance or margin between the reference and popper. It is used internally to create an offset modifier. NB: If you define offset prop, it'll override the gutter.
            has_arrow: If true, the tooltip will show an arrow tip
            is_disabled: If true, the tooltip with be disabled.
            is_open: If true, the tooltip will be open.
            label: The label of the tooltip
            open_delay: Delay (in ms) before showing the tooltip
            placement: The placement of the popper relative to its reference.
            should_wrap_children: If true, the tooltip will wrap its children in a `<span/>` with `tabIndex=0`
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
