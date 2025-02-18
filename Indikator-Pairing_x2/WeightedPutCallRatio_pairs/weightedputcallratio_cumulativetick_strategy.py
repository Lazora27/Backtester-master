import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'CumulativeTick': 1.0
        })
    )
