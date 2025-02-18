import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MarketBalance': 1.0
        })
    )
