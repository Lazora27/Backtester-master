import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'CumulativeTick': 1.0
        })
    )
