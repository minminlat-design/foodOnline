from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def create_profile_post_save_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('User profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            print('Profile was not exit, but i created one')
        print('User is updated')
    
@receiver(pre_save, sender=User)
def profile_pre_save_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')