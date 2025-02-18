import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'SmoothedCycle': 1.0
        })
    )
