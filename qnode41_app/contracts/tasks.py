from qnode41_app.celery import app
from django.core.mail import send_mail
from .models import Contract


@app.task
def contract_created(contract_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    contract = Contract.objects.get(id=contract_id)
    subject = 'Contract nr. {}'.format(contract.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                  Your order id is {}.'.format(contract.first_name,
                                            contract.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [contract.email])
    return mail_sent
