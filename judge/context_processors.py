from django.utils import timezone
from judge.models import Contest

def get_new_contests(request):
    now = timezone.now()
    visible_contests = Contest.get_visible_contests(request.user).filter(is_visible=True) \
                              .order_by('start_time')
    
    contests = []

    if request.user.is_authenticated:
        for contest in visible_contests.filter(start_time__gt=now).all():
            if not request.profile in contest.seen_by.all():
                contest.seen_by.add(request.profile)
                contests.append(contest)
                contest.save()
    
    return {'new_contests': contests}