import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
