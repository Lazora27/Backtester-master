import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
