import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FlowOfFunds': 1.0
        })
    )
