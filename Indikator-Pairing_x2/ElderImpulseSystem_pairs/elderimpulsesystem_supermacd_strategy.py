import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'SuperMACD': 1.0
        })
    )
