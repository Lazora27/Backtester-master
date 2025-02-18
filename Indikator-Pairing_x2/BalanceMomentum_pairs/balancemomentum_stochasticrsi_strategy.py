import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'StochasticRSI': 1.0
        })
    )
