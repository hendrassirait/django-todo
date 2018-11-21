from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
	semua_todo_item = TodoItem.objects.all()
	return render(request, 'todo.html', 
		{'semua_items': semua_todo_item})

def addTodo(request):
# buat todo semua_items baru
	new_item = TodoItem(content = request.POST['content']) 
# save
	new_item.save()
# redirect browser ke "/todo/"
	return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
	item_yang_dihapus = TodoItem.objects.get(id=todo_id)
	item_yang_dihapus.delete()
	return HttpResponseRedirect('/todo/')