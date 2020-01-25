from django.shortcuts import render, redirect
from .models import Buku
from .forms import BukuForm


def buku(request):
	Semua_buku=Buku.objects.all()

	context={
        'page_title':'Daftar Buku',
        'semua_buku':Semua_buku,
	}
	return render(request,'buku/buku.html',context)

def add(request):
	buku_form = BukuForm(request.POST or None)

	if request.method == 'POST':
		if buku_form.is_valid():
			buku_form.save()

		return redirect('buku:buku')

	context = {
		"page_title":"Tambah Buku",
		"buku_form":buku_form,
	}

	return render(request,'buku/tambah.html',context)

def update(request,update_id):
	buku_update = Buku.objects.get(id=update_id)
	
	data = {
        'penulis'	: buku_update.penulis,
		'judul'	    : buku_update.judul,
		'kota'	    : buku_update.kota,
		'penerbit'	: buku_update.penerbit,
        'tahun'	    : buku_update.tahun,
	}
	buku_form = BukuForm(request.POST or None, initial=data, instance=buku_update)

	if request.method == 'POST':
		if buku_form.is_valid():
			buku_form.save()

		return redirect('buku:buku')

	context = {
		"page_title":"Update Buku",
		"buku_form":buku_form,
	}

	return render(request,'buku/tambah.html',context)


def delete(request,delete_id):
	Buku.objects.filter(id=delete_id).delete()
	return redirect('buku:buku')