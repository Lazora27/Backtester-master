import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TrendExhaustion': 1.0
        })
    )
