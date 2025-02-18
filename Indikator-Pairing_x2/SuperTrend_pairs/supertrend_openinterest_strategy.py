import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und OpenInterest
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'OpenInterest': 1.0
        })
    )
