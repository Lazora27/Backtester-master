import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CumulativeTick': 1.0
        })
    )
