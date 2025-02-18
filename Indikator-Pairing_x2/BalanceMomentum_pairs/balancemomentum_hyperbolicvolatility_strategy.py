import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
