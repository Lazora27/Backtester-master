import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
