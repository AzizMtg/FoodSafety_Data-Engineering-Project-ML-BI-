from django.db import models
from owner.models import Facility  # Import the Facility model

VIOLATION_CODE_CHOICES = [
    ('F001', 'F001'), ('F002', 'F002'), ('F003', 'F003'), ('F004', 'F004'),
    ('F005', 'F005'), ('F006', 'F006'), ('F007', 'F007'), ('F008', 'F008'),
    ('F009', 'F009'), ('F010', 'F010'), ('F011', 'F011'), ('F012', 'F012'),
    ('F013', 'F013'), ('F014', 'F014'), ('F015', 'F015'), ('F016', 'F016'),
    ('F017', 'F017'), ('F018', 'F018'), ('F019', 'F019'), ('F021', 'F021'),
    ('F022', 'F022'), ('F023', 'F023'), ('F024', 'F024'), ('F025', 'F025'),
    ('F026', 'F026'), ('F027', 'F027'), ('F028', 'F028'), ('F029', 'F029'),
    ('F030', 'F030'), ('F031', 'F031'), ('F032', 'F032'), ('F033', 'F033'),
    ('F034', 'F034'), ('F035', 'F035'), ('F036', 'F036'), ('F037', 'F037'),
    ('F038', 'F038'), ('F039', 'F039'), ('F040', 'F040'), ('F041', 'F041'),
    ('F042', 'F042'), ('F043', 'F043'), ('F044', 'F044'), ('F045', 'F045'),
    ('F046', 'F046'), ('F047', 'F047'), ('F048', 'F048'), ('F049', 'F049'),
    ('F050', 'F050'), ('F051', 'F051'), ('F052', 'F052'), ('F053', 'F053'),
    ('F054', 'F054'), ('F055', 'F055'), ('F056', 'F056'), ('F057', 'F057'),
    ('F058', 'F058'), ('H102', 'H102'), ('MF08', 'MF08'), ('MF15', 'MF15'),
    ('MF31', 'MF31'), ('MF34', 'MF34'), ('MF36', 'MF36'), ('MF38', 'MF38'),
    ('MF41', 'MF41'), ('MF45', 'MF45'), ('W004', 'W004'), ('W005', 'W005'),
    ('W019', 'W019'), ('W021', 'W021'), ('W023', 'W023'), ('W027', 'W027'),
    ('W028', 'W028'), ('W032', 'W032'), ('W034', 'W034'), ('W041', 'W041'),
    ('W044', 'W044'), ('W051', 'W051'), ('W052', 'W052'),
]

class Inspection(models.Model):
    activity_date = models.DateField()
    score = models.IntegerField()
    grade = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')],
        blank=True
    )
    service_description = models.CharField(
        max_length=100,
        choices=[
            ('ROUTINE INSPECTION', 'ROUTINE INSPECTION'),
            ('OWNER INITIATED ROUTINE INSPECT.', 'OWNER INITIATED ROUTINE INSPECT.')
        ]
    )
    risk = models.CharField(
        max_length=50,
        choices=[
            ('Low Risk', 'Low Risk'),
            ('Moderate Risk', 'Moderate Risk'),
            ('High Risk', 'High Risk')
        ]
    )
    service_code = models.IntegerField(
        choices=[(401, 'OWNER INITIATED'), (402, 'ROUTINE INSPECTION')]
    )
    violation_code = models.CharField(
        max_length=10,
        choices=VIOLATION_CODE_CHOICES,
        default='F001'  # Replace 'F001' with a valid default choice
    )
    
    # Foreign key to Facility (cannot be null)
    facility = models.ForeignKey(
        Facility, 
        on_delete=models.CASCADE, 
        related_name='inspections', 
        verbose_name="Facility",
        null=True  # Make the foreign key non-nullable
    )

    def __str__(self):
        return f"Inspection on {self.activity_date} - Score: {self.score}"