import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AdaptiveATR': 1.0
        })
    )
