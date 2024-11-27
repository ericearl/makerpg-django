INC = 'I'
DEC = 'D'
DIRECTION_CHOICES = (
    (INC, 'increasing'),
    (DEC, 'decreasing'),
)

IND = 'I'
DEP = 'D'
TYPE_CHOICES = (
    (IND, 'independent'),
    (DEP, 'dependent'),
)

TIER_CHOICES = (
    (0, 'add'),
    (1, 'multiply'),
    (2, 'double'),
    (3, 'triple'),
    (4, 'quadruple'),
    (5, 'quintuple'),
    (6, 'sextuple'),
    (7, 'septuple'),
    (8, 'octuple'),
    (9, 'nonuple'),
    (10, 'decuple'),
)

NAME = 'name'
OPERATION_CHOICES = (
    ('name', 'name'),
    ('select', 'select'),
    ('spend', 'spend'),
    ('history', 'history'),
    ('', ''),
    ('', ''),
)
