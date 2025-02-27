# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals
import inspect

# Third party imports
# Local application / specific library imports


class MenuItemMixin(object):
    """
    This mixins injects attributes that start with the 'menu_' prefix into
    the context generated by the view it is applied to.
    This behavior can be used to highlight an item of a navigation component.
    """
    def get_context_data(self, **kwargs):
        context = super(MenuItemMixin, self).get_context_data(**kwargs)
        vattrs = inspect.getmembers(self, lambda a: not(inspect.isroutine(a)))
        menu_kwargs = dict(a for a in vattrs if a[0].startswith('menu_'))
        context.update(menu_kwargs)
        return context
