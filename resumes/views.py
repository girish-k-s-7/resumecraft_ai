from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def builder_page(request):
    return render(
        request,
        "resumes/feature.html",
        {
            "title": "Build Your Resume",
            "description": "Create a professional resume using our resume builder."
        }
    )


def analyzer_page(request):
    return render(
        request,
        "resumes/feature.html",
        {
            "title": "AI Resume Analyzer",
            "description": "Compare your resume with a job description using AI."
        }
    )
