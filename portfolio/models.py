from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
import os

class SkillType(models.TextChoices):
    SQL = 'SQL', _('SQL')
    PY = 'PY', _('Python')
    HTML = 'HTML', _('HTML')
    CSS = 'CSS', _('CSS')
    JS = 'JS', _('JavaScript')
    CPP = 'CPP', _('C++')
    PHP = 'PHP', _('PHP')
    RUST = 'RUST', _('Rust')

class Skill(models.Model):
    code = models.CharField(
        max_length=4,
        choices=SkillType.choices,
        unique=True,
        verbose_name=_('Skill')
    )

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')
        ordering = ['code']

    def __str__(self):
        return self.get_code_display()

class Cv(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cvs',
        verbose_name=_('User')
    )

    work_email = models.EmailField(
        max_length=100,
        verbose_name=_('Work email')
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name=_('Phone number')
    )
    github = models.URLField(
        verbose_name=_('GitHub profile'),
        blank=True
    )
    summary = models.TextField(
        verbose_name=_('Summary')
    )
    skills = models.ManyToManyField(
        Skill,
        related_name='cvs',
        verbose_name=_('Skills')
    )
    work_experience = models.TextField(
        verbose_name=_('Work experience')
    )
    education = models.TextField(
        verbose_name=_('Education')
    )

    class Meta:
        verbose_name = _('CV')
        verbose_name_plural = _('CVs')

    def __str__(self):
        return f'CV: {self.user}'
    
class CvFile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cv_files'
    )
    cv = models.ForeignKey(
        'Cv',
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(
        upload_to='cvs/',
        verbose_name=_('CV file')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('CV file')
        verbose_name_plural = _('CV files')
        ordering = ['-created_at']

    def __str__(self):
        return f'CV file for {self.user}'
    
    @property
    def filename(self):
        return os.path.basename(self.file.name)