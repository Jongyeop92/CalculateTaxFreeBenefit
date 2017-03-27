BENEFIT = "benefit"
LOSS    = "loss"

MINIMUM_TAX_FREE_AMOUNT = 5400
TAX_RATE = 0.08

def getBenefitLoss(amount):

    if amount >= MINIMUM_TAX_FREE_AMOUNT:
        return BENEFIT

    tax_amount = MINIMUM_TAX_FREE_AMOUNT * TAX_RATE
    differ = MINIMUM_TAX_FREE_AMOUNT - amount

    if differ <= tax_amount:
        return LOSS
    else:
        return BENEFIT


def test():
    
    assert getBenefitLoss(1000) == BENEFIT
    assert getBenefitLoss(5000) == LOSS
    assert getBenefitLoss(5399) == LOSS
    assert getBenefitLoss(5400) == BENEFIT

    print "Success"


def main():
    
    start_amount = 4960
    end_amount   = 5410
    amount_gap   = 1

    amount_list = list(range(start_amount, end_amount, amount_gap))

    tax_free_amount_list = []
    for amount in amount_list:
        print amount, getBenefitLoss(amount)


if __name__ == "__main__":
    #test()
    main()
