import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
