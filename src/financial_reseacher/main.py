#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from rich.repr import Result

from financial_reseacher.crew import FinancialReseacherCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the FinancialReseacher crew
    """
    inputs = {
        'company': 'Apple'
    }
    
    Result=FinancialReseacherCrew().crew().kickoff(inputs=inputs)
    print(Result.raw)


if __name__ == "__main__":
    run()
