import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
