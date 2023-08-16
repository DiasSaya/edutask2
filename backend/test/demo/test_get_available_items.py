import pytest
from src.controllers.recipecontroller import RecipeController
from src.util.dao import DAO

# Mock DAO for testing
class MockItemsDAO(DAO):
    def get_all(self):
        # Implement mock behavior for testing
        return []

# Test cases
@pytest.fixture
def recipe_controller():
    return RecipeController(MockItemsDAO())

def test_no_items_in_pantry(recipe_controller):
    available_items = recipe_controller.get_available_items()
    assert available_items == {}

def test_mix_of_items_above_min_quantity(recipe_controller):
    items = [{"name": "item1", "quantity": 1}, {"name": "item2", "quantity": 5}]
    recipe_controller.dao.set_data(items)
    available_items = recipe_controller.get_available_items(minimum_quantity=2)
    assert available_items == {"item2": 5}

def test_all_items_above_min_quantity(recipe_controller):
    items = [{"name": "item1", "quantity": 3}, {"name": "item2", "quantity": 7}]
    recipe_controller.dao.set_data(items)
    available_items = recipe_controller.get_available_items(minimum_quantity=1)
    assert available_items == {"item1": 3, "item2": 7}

def test_all_items_below_min_quantity(recipe_controller):
    items = [{"name": "item1", "quantity": 2}, {"name": "item2", "quantity": 3}]
    recipe_controller.dao.set_data(items)
    available_items = recipe_controller.get_available_items(minimum_quantity=4)
    assert available_items == {}

# Run tests
if __name__ == "__main__":
    pytest.main()
