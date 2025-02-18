import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CumulativeTick': 1.0
        })
    )
