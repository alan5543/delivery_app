
# The main files for the command to call out the API service to query the dB records
# The commands are create_order, list_orders, take_order

import click
from query import listAllProducts, createNewOrder, takeOrder


'''
create-order - Command for Create the New Lalamove Order
'''
@click.group()
def cli1():
    pass

@cli1.command()
@click.argument('_from_')
@click.argument('_to_')
def create_order(_from_, _to_):
    """returns a unique ID for this order. from and to are required"""
    createNewOrder(_from_, _to_)




'''
list-orders -  Command for List all the Orders
'''
@click.group()
def cli2():
    pass

@cli2.command()
def list_orders():
    """List all the available (non-taken) orders with this format"""
    listAllProducts()





'''
take-order -  Command for take the order according to the product ID
'''
@click.group()
def cli3():
    pass

@cli3.command()
@click.argument('id')
def take_order(id):
    """Try to take the order with the given ID, returns an error if order is already taken. id is required"""
    takeOrder(id)




cli = click.CommandCollection(sources=[cli1, cli2, cli3])

if __name__ == '__main__':
    cli()