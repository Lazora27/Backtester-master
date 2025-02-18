import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'WeightedCycle': 1.0
        })
    )
