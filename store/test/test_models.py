from store.models import Product, Category
from django.contrib.auth.models import User
from django.test import TestCase

class TestProductModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name="Fiction",
            slug="fiction"
        )

        self.product = Product.objects.create(
            category=self.category,
            created_by=self.user,
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
        self.assertEqual(str(self.product), "Sample Book")
        self.assertEqual(self.product.created_by.username, "testuser")
        self.assertEqual(self.product.category.name, "Fiction")

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Sample Book")

    def test_product_relationships(self):
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.created_by, self.user)

    def test_product_defaults(self):
        product2 = Product.objects.create(
            category=self.category,
            created_by=self.user,
            title="Another Book",
            slug="another-book",
            price=29.99
        )
        self.assertEqual(product2.author, "admin")

class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Non-Fiction", slug="non-fiction")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Non-Fiction")
        self.assertEqual(self.category.slug, "non-fiction")
        self.assertEqual(str(self.category), "Non-Fiction")
