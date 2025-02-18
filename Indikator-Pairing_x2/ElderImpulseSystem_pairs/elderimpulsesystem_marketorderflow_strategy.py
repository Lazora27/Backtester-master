import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
