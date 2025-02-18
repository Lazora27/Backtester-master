import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AutoFibonacci': 1.0
        })
    )
