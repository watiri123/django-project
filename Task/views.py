from django.shortcuts import render

# Create your views here.
tasks = ["buy groceries", "watch football", "go home"]


def Task(request):
    return render(request, "task.html", {

        "tasks": tasks

    })
def add(request):
    return render(request, "add.html")

