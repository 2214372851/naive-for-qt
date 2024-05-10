from enum import Enum


class Size(Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'
    huge = 'huge'


class Switch(Enum):
    on = 'true'
    off = 'false'


class ButtonType(Enum):
    text = 'text'
    default = 'default'
    tertiary = 'tertiary'
    info = 'info'
    success = 'success'
    warning = 'warning'
    error = 'error'
    dashed_default = 'dashed-default'
    dashed_tertiary = 'dashed-tertiary'
    dashed_info = 'dashed-info'
    dashed_success = 'dashed-success'
    dashed_warning = 'dashed-warning'
    dashed_error = 'dashed-error'
    secondary_default = 'secondary-default'
    secondary_tertiary = 'secondary-tertiary'
    secondary_info = 'secondary-info'
    secondary_success = 'secondary-success'
    secondary_warning = 'secondary-warning'
    secondary_error = 'secondary-error'
    tertiary_default = 'tertiary-default'
    tertiary_tertiary = 'tertiary-tertiary'
    tertiary_info = 'tertiary-info'
    tertiary_success = 'tertiary-success'
    tertiary_warning = 'tertiary-warning'
    tertiary_error = 'tertiary-error'


class TagType(Enum):
    default = 'default'
    info = 'info'
    success = 'success'
    warning = 'warning'
    error = 'error'


class TextType(Enum):
    default = 'default'
    info = 'info'
    success = 'success'
    warning = 'warning'
    error = 'error'


