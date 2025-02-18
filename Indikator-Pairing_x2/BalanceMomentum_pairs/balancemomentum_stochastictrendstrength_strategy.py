import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
