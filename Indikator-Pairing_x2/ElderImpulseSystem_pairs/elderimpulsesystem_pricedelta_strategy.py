import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PriceDelta
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PriceDelta': 1.0
        })
    )
