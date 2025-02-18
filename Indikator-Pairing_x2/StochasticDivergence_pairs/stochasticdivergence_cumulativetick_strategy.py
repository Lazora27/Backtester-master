import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CumulativeTick': 1.0
        })
    )
