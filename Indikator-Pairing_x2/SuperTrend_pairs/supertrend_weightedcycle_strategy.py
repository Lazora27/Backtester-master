import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'WeightedCycle': 1.0
        })
    )
