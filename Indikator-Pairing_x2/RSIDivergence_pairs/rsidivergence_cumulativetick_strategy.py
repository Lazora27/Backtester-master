import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CumulativeTick': 1.0
        })
    )
