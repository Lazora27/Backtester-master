import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'BuyingPressure': 1.0
        })
    )
