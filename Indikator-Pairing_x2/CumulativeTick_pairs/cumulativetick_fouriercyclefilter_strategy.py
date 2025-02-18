import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
