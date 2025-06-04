from django.core.management.base import BaseCommand
from django.utils import timezone
from exam.models import Question, StudentExamScore
from essay.models import QuestionBank, StudentResponse

class Command(BaseCommand):
    help = 'Deletes tests and responses that are older than 24 hours.'

    def handle(self, *args, **kwargs):
        expiration_time = timezone.now() - timezone.timedelta(hours=24)

        # Delete expired MCQ tests
        expired_mcq_tests = Question.objects.filter(created_at__lt=expiration_time).values_list('title', flat=True)
        if expired_mcq_tests:
            StudentExamScore.objects.filter(test_title__in=expired_mcq_tests).delete()
            Question.objects.filter(title__in=expired_mcq_tests).delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted {len(expired_mcq_tests)} expired MCQ tests.'))

        # Delete expired Subjective tests
        expired_subjective_tests = QuestionBank.objects.filter(created_at__lt=expiration_time).values_list('exam_title', flat=True)
        if expired_subjective_tests:
            StudentResponse.objects.filter(exam_title__in=expired_subjective_tests).delete()
            QuestionBank.objects.filter(exam_title__in=expired_subjective_tests).delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted {len(expired_subjective_tests)} expired subjective tests.'))

        self.stdout.write(self.style.SUCCESS('Expired tests deletion completed.'))
