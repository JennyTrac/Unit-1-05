# Created by: Jenny Trac
# Created on: Sept 26 2017
# Group members: Andre, Malcolm
# This program calculates cost of a pizza when given diameter

import ui

def calculate_touch_up_inside(sender):
    # button to calculate cost of pizza
    
    # input
    diameter = float(view['diameter_textfield'].text)
    LABOUR = 0.75
    RENT = 1.00
    TAX = 1.13
    
    # calculate
    cost = ( LABOUR + RENT + 0.5 * diameter ) * TAX
    
    # output
    view['cost_label'].text = "Cost of the pizza is: " + '${:,.2f}'.format(cost)
    
view = ui.load_view()
view.present('sheet')
