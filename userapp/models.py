from django.db import models

# Create your models here.
import re
from django.db import models
from django.utils import timezone


class Statistics(models.Model):
    clients_count = models.IntegerField(default=0)
    projects_count = models.IntegerField(default=0)
    upcoming_projects_count = models.IntegerField(default=0)
    events_count = models.IntegerField(default=0)

    def __str__(self):
        return "Statistics"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name


class Project(models.Model):
    project_first_name = models.CharField(max_length=200)
    project_last_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    who_we_are = models.TextField()
    our_impact = models.TextField()

    def __str__(self):
        return f"{self.project_first_name} {self.project_last_name}"


class WhatWeOffer(models.Model):
    project = models.ForeignKey(Project, related_name='offers', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class SDG(models.Model):
    project = models.ForeignKey(Project, related_name='sdgs', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sdg_images/')

    def __str__(self):
        return f"SDG for {self.project.project_first_name} {self.project.project_last_name}"


class Event(models.Model):
    EVENT_STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('upcoming', 'Upcoming'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.ImageField(upload_to='event_images/')
    status = models.CharField(max_length=10, choices=EVENT_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Gallery Image {self.id}"


class HighlightMedia(models.Model):
    video = models.FileField(upload_to='highlight_videos/')
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Highlight Video {self.id}"


class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('local', 'Local Video'),
        ('youtube', 'YouTube Video'),
    ]

    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    video_file = models.FileField(upload_to='media_videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.media_type == 'youtube' and self.video_url:
            self.video_url = self.extract_video_id(self.video_url)
        super(Media, self).save(*args, **kwargs)

    @staticmethod
    def extract_video_id(url):
        # Regex to extract the video ID from various YouTube URL formats
        regex = (
            r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)|.*[?&]v=)|'
            r'youtu\.be/)([^"&?/ ]{11})'
        )
        match = re.match(regex, url)
        if match:
            return match.group(1)
        return url


class JobOpening(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    position = models.ForeignKey(JobOpening, on_delete=models.SET_NULL, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    message = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position.title if self.position else 'Unknown Position'}"


class SupportMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

