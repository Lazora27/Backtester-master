import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und PriceDelta
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'PriceDelta': 1.0
        })
    )
