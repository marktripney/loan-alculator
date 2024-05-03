import argparse
import math
import sys


def calc_value_of_annuity_payments(prin, per, inter):
    one_plus_interest_to_power_periods = (1 + inter) ** per
    monthly_annuity = prin * (
            (inter * one_plus_interest_to_power_periods) /
            (one_plus_interest_to_power_periods - 1))
    print(f"Your annuity payment = {math.ceil(monthly_annuity)}!")
    overpayment = (math.ceil(monthly_annuity) * per) - prin
    print(f"Overpayment = {int(overpayment)}")


def calc_value_of_diff_payments(prin, per, inter):
    payment_schedule = []
    for month in range(1, per + 1):
        monthly_payment = prin / per + inter * (prin - (prin * (month - 1) / per))
        payment_schedule.append(math.ceil(monthly_payment))
        print(f"Month {month}: payment is {math.ceil(monthly_payment)}")
    print(f"\nOverpayment = {int(sum(payment_schedule) - prin)}")


def calc_loan_principal(pay, per, inter):
    one_plus_interest_to_power_periods = (1 + inter) ** per
    principal = pay / (
            (inter * one_plus_interest_to_power_periods) /
            (one_plus_interest_to_power_periods - 1))
    print(f"Your loan principal = {math.floor(principal)}!")
    overpayment = (pay * per) - principal
    print(f"Overpayment = {math.ceil(overpayment)}")


def calc_number_of_monthly_payments(prin, pay, inter):
    periods = math.log(pay / (pay - inter * prin), 1 + inter)
    months_to_pay = math.ceil(periods)
    years, months = divmod(months_to_pay, 12)
    if months == 0:
        print(f"It will take {years} to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    overpayment = (months_to_pay * pay) - prin
    print(f"Overpayment = {math.ceil(overpayment)}")


def main():
    parser = argparse.ArgumentParser(
        description='Calculate loan parameters: number of monthly payments; value '
                    'of monthly payments; or loan principal')

    parser.add_argument("--type")
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")

    args = parser.parse_args()

    loan_parameters = [args.type, args.payment, args.principal, args.periods, args.interest]

    if loan_parameters.count(None) > 1:
        print("Incorrect parameters")
        sys.exit()
    payment_type, payment, principal, periods, interest = loan_parameters

    for value in [payment, principal, periods, interest]:
        if value and float(value) < 0:
            print("Incorrect parameters")
            sys.exit()

    if interest is None:
        print("Incorrect parameters")
        sys.exit()
    else:
        monthly_interest = (float(interest) / 12) / 100

    if payment_type not in ["annuity", "diff"]:
        print("Incorrect parameters.")
    elif payment_type == 'diff' and payment is None:
        calc_value_of_diff_payments(float(principal), int(periods), monthly_interest)
    elif payment_type == 'diff' and payment:
        raise SystemExit("Incorrect parameters")
    elif payment_type == 'annuity' and payment is None:
        calc_value_of_annuity_payments(float(principal), int(periods), monthly_interest)
    elif principal is None:
        calc_loan_principal(float(payment), int(periods), monthly_interest)
    elif periods is None:
        calc_number_of_monthly_payments(float(principal), float(payment), monthly_interest)
    else:
        print("Incorrect parameters.")


if __name__ == "__main__":
    main()
