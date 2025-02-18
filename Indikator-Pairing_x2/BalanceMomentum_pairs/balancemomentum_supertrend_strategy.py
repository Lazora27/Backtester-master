import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SuperTrend
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SuperTrend': 1.0
        })
    )
