import pytest
from products import Product

def test_create_normal_product():
    product = Product("Laptop", 1500, 10)
    assert product.name == "Laptop"
    assert product.price == 1500
    assert product.quantity == 10
    assert product.is_active() is True

def test_create_product_with_empty_name():
    with pytest.raises(ValueError) as excinfo:
        Product("", 1450, 100)
    assert "Product name cannot be empty" in str(excinfo.value)

def test_create_product_with_negative_price():
    with pytest.raises(ValueError) as excinfo:
        Product("MacBook Air M2", -10, 100)
    assert "Product price cannot be negative" in str(excinfo.value)

def test_create_product_with_negative_quantity():
    with pytest.raises(ValueError) as excinfo:
        Product("MacBook Air M2", 1000, -10)
    assert "Product quantity cannot be negative" in str(excinfo.value)

def test_product_becomes_inactive_when_quantity_zero():
    product = Product("Phone", 1000, 1)
    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False

def test_product_purchase_modifies_quantity():
    product = Product("Tablet", 500, 5)
    remaining_quantity = product.buy(3)
    assert remaining_quantity == 2
    assert product.quantity == 2

def test_purchase_larger_quantity_than_exists():
    product = Product("Headphones", 200, 2)
    with pytest.raises(ValueError) as excinfo:
        product.buy(3)
    assert "Not enough quantity in stock." in str(excinfo.value)
