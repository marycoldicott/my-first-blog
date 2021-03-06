from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import cv_page
from lists.views import cv_add_photo
from django.template.loader import render_to_string
from lists.models import Area, Item

# Create your tests here.
class CVPageTest(TestCase):

	def test_uses_base_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'blog/base.html')

	def test_cv_url(self):
		found = resolve('/cv/')
		self.assertEqual(found.func, cv_page)

	def test_redirect_add(self):
		found = resolve('/cv/photo')
		self.assertEqual(found.func, cv_add_photo)

class NewItemAreaTest(TestCase):

	def test_can_create_a_new_area(self):
		self.client.post(
			f'/cv/photo/create',
			{'type_': 'photo'},
		)

		self.client.post(
			f'/cv/photo/create',
			{'type_': 'experience'},
		)

		self.assertEqual(Area.objects.count(), 2)
		new_area = Area.objects.first()
		self.assertEqual(new_area.area_type, 'photo')
		new_area_2 = Area.objects.filter(area_type='experience')
		if new_area_2:
			new_area_2 = new_area_2[0]
		self.assertEqual(new_area_2.area_type, 'experience')


	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = Area.objects.create(area_type='experience')
		correct_list = Area.objects.create(area_type='photo')

		self.client.post(
			f'/cv/photo/add_item',
			{'item_text[]': 'A photo url', 'type_': 'photo', 'item_type': 'url'},
		)

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A photo url\n')
		self.assertEqual(new_item.area, correct_list)

	def test_redirects_to_list_view(self):
		other_area = Area.objects.create(area_type="experience")
		correct_area = Area.objects.create(area_type="photo")

		response = self.client.post(
			f'/cv/photo/add_item',
			{'item_text': 'A photo url', 'type_': 'photo', 'item_type': 'url'}
		)

		self.assertRedirects(response, f'/cv/')

class CVAddPageTest(TestCase):

	def test_saving_and_retrieving_items(self):
		area_ = Area()
		area_.area_type = 'photo'
		area_.save()
		self.assertEqual(area_.area_type, 'photo')

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.area = area_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.area = area_
		second_item.save()

		saved_list = Area.objects.first()
		self.assertEqual(saved_list, area_)
		self.assertEqual(saved_list.area_type, area_.area_type)
		#self.assertEqual(saved_list[0].text, first_item.text)

		self.assertEqual(second_item.area.area_type, area_.area_type)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.area, area_)
		self.assertEqual(first_saved_item.area.area_type, 'photo')
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.area, area_)
		self.assertEqual(second_saved_item.area.area_type, 'photo')

class CVDetail(TestCase):

	def test_detail_shows_correct_item(self):
		area = Area.objects.create(area_type="personal")

		self.client.post(
			f'/cv/personal/add_item',
			{'item_text[]': 'Mary', "type_": "personal", "item_type": 'Name'}
		)

		self.assertEqual(Item.objects.count(), 1)

		self.client.post(
			f'/cv/personal/add_item',
			{'item_text[]': 'mary.coldicott@gmail.com', "type_": "personal", "item_type": 'Email'}
		)

		self.assertEqual(Item.objects.count(), 2)

		item = Item.objects.first()
		pk = item.pk


class DeleteItemTest(TestCase):

	def test_deleting_personal_info(self):
		personal_area = Area.objects.create(area_type="personal")

		self.client.post(
			f'/cv/personal/add_item',
			{'item_text[]': 'Mary', "type_": "personal", "item_type": 'Name'}
		)

		self.assertEqual(Item.objects.count(), 1)
		item = Item.objects.first()
		self.assertEqual(item.text, "Mary\n")

		self.client.post(
			f'/cv/personal/{item.pk}/delete/',
		)

		self.assertEqual(Item.objects.count(), 0)

