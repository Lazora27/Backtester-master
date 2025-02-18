import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'CenterOfGravity': 1.0
        })
    )
