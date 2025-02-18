import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AverageLogRange': 1.0
        })
    )
