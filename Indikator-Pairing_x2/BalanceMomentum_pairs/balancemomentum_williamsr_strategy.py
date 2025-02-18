import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und WilliamsR
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'WilliamsR': 1.0
        })
    )
