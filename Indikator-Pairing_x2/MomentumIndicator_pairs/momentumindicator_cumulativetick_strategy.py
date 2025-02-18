import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'CumulativeTick': 1.0
        })
    )
