import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
