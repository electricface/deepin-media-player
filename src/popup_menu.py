#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Deepin, Inc.
#               2012 Hailong Qiu
#
# Author:     Hailong Qiu <356752238@qq.com>
# Maintainer: Hailong Qiu <356752238@qq.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class PopupMenu(object):
    def __init__(self):
        
        
        
        
        
        
        
        
        
        
'''        
sub_menu_a = Menu(
        [(ui_theme.get_pixbuf("menu/menuItem1.png"), "子菜单A1", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem2.png"), "子菜单A2", None),
         (ui_theme.get_pixbuf("menu/menuItem3.png"), "子菜单A3", None),
         ])
    sub_menu_e = Menu(
        [(ui_theme.get_pixbuf("menu/menuItem1.png"), "子菜单E1", None),
         (ui_theme.get_pixbuf("menu/menuItem2.png"), "子菜单E2", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem3.png"), "子菜单E3", None),
         ])
    sub_menu_d = Menu(
        [(ui_theme.get_pixbuf("menu/menuItem1.png"), "子菜单D1", None),
         (ui_theme.get_pixbuf("menu/menuItem2.png"), "子菜单D2", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem3.png"), "子菜单D3", sub_menu_e),
         ])
    sub_menu_c = Menu(
        [(ui_theme.get_pixbuf("menu/menuItem1.png"), "子菜单C1", None),
         (ui_theme.get_pixbuf("menu/menuItem2.png"), "子菜单C2", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem3.png"), "子菜单C3", sub_menu_d),
         ])
    sub_menu_b = Menu(
        [(ui_theme.get_pixbuf("menu/menuItem1.png"), "子菜单B1", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem2.png"), "子菜单B2", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem3.png"), "子菜单B3", sub_menu_c),
         ])
    
    menu = Menu(
        [(ui_theme.get_pixbuf("menu/menuItem1.png"), "测试测试测试1", lambda : PopupWindow(application.window)),
         (ui_theme.get_pixbuf("menu/menuItem2.png"), "测试测试测试2", sub_menu_a),
         (ui_theme.get_pixbuf("menu/menuItem3.png"), "测试测试测试3", sub_menu_b),
         None,
         (None, "测试测试测试", None),
         (None, "测试测试测试", None),
         None,
         (ui_theme.get_pixbuf("menu/menuItem6.png"), "测试测试测试4", None, (1, 2, 3)),
         (ui_theme.get_pixbuf("menu/menuItem7.png"), "测试测试测试5", None),
         (ui_theme.get_pixbuf("menu/menuItem8.png"), "测试测试测试6", None),
         ],
        True
        )
    application.set_menu_callback(lambda button: menu.show(
            get_widget_root_coordinate(button, WIDGET_POS_BOTTOM_LEFT),
            (button.get_allocation().width, 0)))
            
'''    