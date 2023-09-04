from account_class import *
from asset_class import *
from liability_class import *
from OE_classes import *
from trial_balance_class import *
from prettytable import PrettyTable


class FinancialPosition:
    def __init__(self) -> None:
        __class__.table.add_row(["Assets", "", ""])
        __class__.make_row(__class__.assets)
        __class__.table.add_row(
            ["Total Assets", "", __class__.assets_total_balance], divider=True
        )
        __class__.table.add_row(
            [
                "Liabilites and Owner's Equity",
                "",
                "",
            ]
        )
        __class__.table.add_row(["Liabilites", "", ""])
        __class__.make_row(__class__.liabs)
        __class__.table.add_row(
            ["Total Liabilites", "", __class__.liabs_total_balance], divider=True
        )
        __class__.table.add_row(["Owner's Equity", "", ""])
        __class__.make_row(__class__.OEs)
        __class__.table.add_row(
            ["Total Owner's Equity", "", __class__.OEs_total_balance], divider=True
        )
        __class__.table.add_row(
            [
                "Total Liabilites and Owner's Equity",
                "",
                __class__.liabs_total_balance + __class__.OEs_total_balance,
            ]
        )

    assets = Asset.class_childs
    assets_names = [acc.name for acc in assets]
    assets_total_balance = sum(acc.balance for acc in assets)
    table = PrettyTable(["Account", "Subtotal", "Total"])
    table.align["Total"] = "r"
    table.set_style(SINGLE_BORDER)
    liabs = Liab.class_childs
    liabs_total_balance = sum(acc.balance for acc in liabs)
    liabs_names = [acc.name for acc in liabs]

    OEs = OE.class_childs
    capitals = Capital.class_childs
    reveneus = Revenue.class_childs
    expenses = Expense.class_childs
    drawings = Drawing.class_childs
    OEs_total_balance = (
        sum(acc.balance for acc in capitals)
        + sum(acc.balance for acc in reveneus)
        - sum(acc.balance for acc in expenses)
        - sum(acc.balance for acc in drawings)
    )

    OEs_names = [acc.name for acc in OEs]

    def make_row(gacc: list):
        k = 0
        n = len(gacc)
        gacc_names = [acc.name for acc in gacc]
        while k < n:
            # if gacc[k].acc_type == "dr":
            # __class__.debit_sum_list.append(gacc[k].balance)
            __class__.table.add_row(
                [
                    gacc_names[k],
                    gacc[k].balance,
                    "",
                ]
            )
            k += 1

    def __str__(self) -> str:
        return str(__class__.table)


x = FinancialPosition()
print(x)