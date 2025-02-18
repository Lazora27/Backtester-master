import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'CumulativeTick': 1.0
        })
    )
