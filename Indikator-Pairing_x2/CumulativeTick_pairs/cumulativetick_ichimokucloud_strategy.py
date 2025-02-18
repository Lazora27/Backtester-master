import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'IchimokuCloud': 1.0
        })
    )
