from datetime import datetime, timedelta

def get_invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY): ")
    invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
    return invoice_date

def main():
    print("The Invoice Due Date Program")
    print()

    while True:
        invoice_date = get_invoice_date()
        print()
        due_date = invoice_date + timedelta(days=30)
        current_date = datetime.now()
        days_overdue = (current_date - due_date).days

        print("Invoice Date:", invoice_date.strftime("%B %d %Y"))
        print("Due Date:", due_date.strftime("%B %d %Y"))
        print("Current Date:", current_date.strftime("%B %d %Y"))

        if days_overdue > 0:
            print("This invoice is " + days_overdue + " day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in " + str(days_due) + " day(s).")
        print()

        result = input("Continue? (y/n): ")
        print()

        if result.lower() != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
