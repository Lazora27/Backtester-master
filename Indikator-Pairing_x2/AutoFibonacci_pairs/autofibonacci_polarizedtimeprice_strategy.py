import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
