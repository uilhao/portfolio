from django.shortcuts import render


def home(request):
    model = {
        'title': 'William Pickens',
        'year': '2020',
    }

    return render(request, 'home/index.html', model)


def about(request):
    model = {
        'title': 'About',
        'year': '2020',
    }

    return render(request, 'about/index.html', model)


def contact(request):
    model = {
        'title': 'Contact',
        'year': '2020',
    }

    return render(request, 'contact/index.html', model)


def skills(request):
    model = {
        'title': 'Skills',
        'year': '2020',
    }

    skills = [
        {
            'name': 'Python',
            'level': 88,
        },
        {
            'name': 'PHP',
            'level': 95,
        },
        {
            'name': 'PySpark/Apache Spark',
            'level': 83,
        },
        {
            'name': 'SQL',
            'level': 90,
        },
        {
            'name': 'Java Script',
            'level': 79,
        },
        {
            'name': 'Bash',
            'level': 70,
        },
    ]
    model['skills'] = skills

    tools = [
        {
            'name': 'AWS',
            'level': 85,
        },
        {
            'name': 'LAMP',
            'level': 85,
        },
        {
            'name': 'Nginx',
            'level': 85,
        },
        {
            'name': 'Docker',
            'level': 80,
        },
        {
            'name': 'Git',
            'level': 90,
        },
        {
            'name': 'SVN',
            'level': 90,
        },
        {
            'name': 'WordPress',
            'level': 97,
        },
        {
            'name': 'Flask',
            'level': 80,
        },
        {
            'name': 'Django',
            'level': 70,
        }
    ]
    model['tools'] = tools

    return render(request, 'skills/index.html', model)


def portfolio(request):
    model = {
        'title': 'Portfolio',
        'year': '2020',
    }

    return render(request, 'portfolio/index.html', model)
