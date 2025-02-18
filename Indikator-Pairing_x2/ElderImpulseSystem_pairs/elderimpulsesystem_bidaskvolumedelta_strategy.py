import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
