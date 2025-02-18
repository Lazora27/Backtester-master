import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
