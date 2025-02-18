import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BalanceMomentum': 1.0
        })
    )
