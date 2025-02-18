import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SuperTrend': 1.0
        })
    )
