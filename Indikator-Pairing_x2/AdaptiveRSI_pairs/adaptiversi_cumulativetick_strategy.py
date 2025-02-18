import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CumulativeTick': 1.0
        })
    )
