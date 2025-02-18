import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
