import test_email.email_handler as eh

TEST_SENDER = "test_sender"
TEST_SENDER_EMAIL = "test@sender.com"
TEST_RECIPIENT = "test_recipient"
TEST_RECIPIENT_EMAIL = "test@recipient.com"
TEST_SUBJECT = "test_subject"
TEST_MESSAGE = "test_message"


def main():
    eh.send_mail(
        TEST_SENDER, TEST_SENDER_EMAIL, 
        TEST_RECIPIENT, TEST_RECIPIENT_EMAIL,
        TEST_SUBJECT,
        TEST_MESSAGE
    )

if __name__ == "__main__":
    main()