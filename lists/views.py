from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from lists.models import Area, Item

# Create your views here.
def cv_page(request):
	#area_ = Area.objects.all();\
	#Area.objects.all().delete()
	area_photo = Area.objects.filter(area_type='photo')
	if area_photo:
		area_photo = area_photo[0]

	area_personal = Area.objects.filter(area_type="personal")
	if area_personal:
		area_personal = area_personal[0]
		area_personal_name = area_personal.item_set.all().filter(item_type="Name").last()
		area_personal_email = area_personal.item_set.all().filter(item_type="Email").last()
		area_personal_mobile = area_personal.item_set.all().filter(item_type="Telephone Number").last()

	area_education = Area.objects.filter(area_type="education")
	if area_education:
		area_education = area_education[0]

	area_experience = Area.objects.filter(area_type="experience")
	if area_experience:
		area_experience = area_experience[0]

	area_skills = Area.objects.filter(area_type="skills")
	if area_skills:
		area_skills = area_skills[0]

	return render(request, 'cv.html', {'area_photo': area_photo, 'area_personal': area_personal,
		"area_personal_name": area_personal_name, "area_personal_email": area_personal_email, "area_personal_mobile": area_personal_mobile,
		"area_education": area_education, "area_experience": area_experience, "area_skills": area_skills})

def cv_add_photo(request):
	area_ = Area.objects.filter(area_type='photo')
	count = area_.count()
	if count > 0:
		create = False
	else:
		create = True

	if area_:
		area_ = area_[0]
	return render(request, 'cv_add_photo.html', {'area': area_, 'create': create})

def cv_add_personal(request):
	area_ = Area.objects.filter(area_type='personal')
	count = area_.count()
	if count > 0:
		create = False
	else:
		create = True

	if area_:
		area_ = area_[0]
	return render(request, 'cv_add_personal.html', {'area': area_, 'create': create})

def cv_add_education(request):
	area_ = Area.objects.filter(area_type='education')
	count = area_.count()
	if count > 0:
		create = False
	else:
		create = True

	if area_:
		area_ = area_[0]
	return render(request, 'cv_add_education.html', {'area': area_, 'create': create})

def cv_add_experience(request):
	area_ = Area.objects.filter(area_type='experience')
	count = area_.count()
	if count > 0:
		create = False
	else:
		create = True

	if area_:
		area_ = area_[0]
	return render(request, 'cv_add_experience.html', {'area': area_, 'create': create})

def cv_add_skills(request):
	area_ = Area.objects.filter(area_type='skills')
	count = area_.count()
	if count > 0:
		create = False
	else:
		create = True

	if area_:
		area_ = area_[0]
	return render(request, 'cv_add_skills.html', {'area': area_, 'create': create})

def detail_personal(request, pk):
	area = Area.objects.filter(area_type="personal")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	return render(request, 'cv_detail.html', {'item': post}, {'area': area})

def detail_education(request, pk):
	area = Area.objects.filter(area_type="education")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	return render(request, 'cv_detail.html', {'item': post}, {'area': area})

def detail_experience(request, pk):
	area = Area.objects.filter(area_type="experience")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	return render(request, 'cv_detail.html', {'item': post}, {'area': area})

def detail_skills(request, pk):
	area = Area.objects.filter(area_type="skills")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	return render(request, 'cv_detail.html', {'item': post}, {'area': area})

def delete_personal(request, pk):
	area = Area.objects.filter(area_type="personal")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	post.delete()
	return render(request, "cv_add_personal.html", {'area':area, 'create': False})

def delete_education(request, pk):
	area = Area.objects.filter(area_type="education")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	post.delete()
	return render(request, "cv_add_education.html", {'area':area, 'create': False})

def delete_experience(request, pk):
	area = Area.objects.filter(area_type="experience")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	post.delete()
	return render(request, "cv_add_experience.html", {'area':area, 'create': False})

def delete_skills(request, pk):
	area = Area.objects.filter(area_type="skills")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)
	post.delete()
	return render(request, "cv_add_skills.html", {'area':area, 'create': False})

def edit_personal(request, pk):
	area = Area.objects.filter(area_type="personal")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)

	if request.method == "POST":
		post.save()
		'''
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			#redirect_address = 'detail_' + a_type
			return redirect('detail_personal', pk=post.pk)
		'''
		return redirect('detail_personal', pk=post.pk)
	else:
		#form = PostForm(instance=post)
		return render(request, 'cv_detail.html', {'form': form})
	

def edit_education(request, pk):
	area = Area.objects.filter(area_type="education")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('detail_education', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'cv_detail.html', {'form': form})

def edit_experience(request, pk):
	area = Area.objects.filter(area_type="experience")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('detail_experience', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'cv_detail.html', {'form': form})

def edit_skills(request, pk):
	area = Area.objects.filter(area_type="skills")
	if area:
		area = area[0]
	items = area.item_set.all()
	post = get_object_or_404(items, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('detail_skills', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'cv_detail.html', {'form': form})

def new_area(request):
	area = Area.objects.create(area_type=request.POST.get('type_', ""))
	#Item.objects.create(text=request.POST['item_text'], list=area)
	return redirect(f'/cv/')

def add_item(request):
	area = Area.objects.filter(area_type=request.POST.get('type_', ""))
	if area:
		area = area[0]
	text_arrays = request.POST.getlist('item_text[]', "")
	text = ""
	for i in range(len(text_arrays)):
		text = text + text_arrays[i] + "\n"
	Item.objects.create(text=text, item_type=request.POST.get('item_type', ""), area=area)
	return redirect(f'/cv/')