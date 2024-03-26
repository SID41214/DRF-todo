from rest_framework.test import APITestCase
from api.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user=User.objects.create_user('usenam','us@gmail.com','password@123')
        self.assertIsInstance(user,User)
        # self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'us@gmail.com')
  
  
    def test_creates_super_user(self):
        user=User.objects.create_superuser('usenam','us@gmail.com','password@123')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'us@gmail.com')
        
    def test_raise_error_when_no_username(self):
        self.assertRaises(ValueError,User.objects.create_user,username='',email='us@gmail.com',password='password@123')
        # self.assertRaisesMessage(ValueError,"The given username must be set")
        # user=User.objects.create_user(username='usenam',email='us@gmail.com',password='password@123')
        # self.assertIsInstance(user,User)
        # self.assertFalse(user.is_staff)
        # self.assertEqual(user.email,'us@gmail.com')
    
    
    def test_raise_with_error_msg(self):
        with self.assertRaisesMessage(ValueError,"The given username must be set"):
            User.objects.create_superuser(username='',email='us@gmail.com',password='password@123')
  
  
    def test_raise_error_when_no_email(self):
        self.assertRaises(ValueError,User.objects.create_user,username='usenam',email='',password='password@123')
        
    
    def test_creates_superuser_status(self):
         with self.assertRaisesMessage(ValueError,"Superuser must have is_staff=True"):
            User.objects.create_superuser(username='usernam',email='us@gmail.com',password='password@123',is_staff=False)
  
    def test_creates_superuser_status_two(self):
         with self.assertRaisesMessage(ValueError,"Superuser must have is_superuser=True"):
            User.objects.create_superuser(username='usernam',email='us@gmail.com',password='password@123',is_superuser=False)
  