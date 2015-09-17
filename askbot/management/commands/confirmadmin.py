from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User

class Command(NoArgsCommand):
    def handle_noargs(self, *args, **kwargs):
		if User.objects.all().count() == 0:
			user = User.objects.create_user('Admin', 'aws@clover.com', '3%JF@j!q!JykZY')
			user.is_superuser = '1'
			user.is_staff = '1'
			user.status = 'd'
			user.save()
			# self.stdout.write('Added admin account "admin"')
		else:
			user = User.objects.get(pk=1)
			user.is_superuser = '1'
			user.is_staff = '1'
			user.status = 'd'
			user.save()
			# self.stdout.write('Set admin status for user "%s"' % user.username)




