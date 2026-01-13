from store.models import Product, Category
from django.test import TestCase

""" class TestProductModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fiction", slug="fiction")
        self.product = Product.objects.create(
            category=self.category,
            created_by_id=1,  # Assuming a user with ID 1 exists
            title="Sample Book",
            author="John Doe",
            description="A sample book description.",
            slug="sample-book",
            price=19.99,
            in_stock=True,
            is_active=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.title, "Sample Book")
        self.assertEqual(self.product.author, "John Doe")
        self.assertEqual(self.product.price, 19.99)
        self.assertTrue(self.product.in_stock)
        self.assertTrue(self.product.is_active)
        self.assertEqual(str(self.product), "Sample Book") """

class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Non-Fiction", slug="non-fiction")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Non-Fiction")
        self.assertEqual(self.category.slug, "non-fiction")
        self.assertEqual(str(self.category), "Non-Fiction")
