import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
