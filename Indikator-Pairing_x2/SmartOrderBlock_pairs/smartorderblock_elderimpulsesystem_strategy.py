import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
