import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und Fisher
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'Fisher': 1.0
        })
    )
