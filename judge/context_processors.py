from django.utils import timezone

from judge.models import Contest


def get_new_contests(request):
    now = timezone.now()
    visible_contests = Contest.get_visible_contests(request.user).filter(is_visible=True) \
                              .order_by('start_time')

    contests = visible_contests.filter(start_time__gt=now).all()

    return {'new_contests': contests}
