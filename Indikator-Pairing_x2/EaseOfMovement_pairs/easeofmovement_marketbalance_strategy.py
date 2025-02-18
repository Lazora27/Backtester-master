import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und MarketBalance
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'MarketBalance': 1.0
        })
    )
