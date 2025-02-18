import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'OpenInterest': 1.0
        })
    )
