import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MarketBalance': 1.0
        })
    )
