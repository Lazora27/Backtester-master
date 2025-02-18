import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
