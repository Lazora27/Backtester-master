import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und GannFans
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'GannFans': 1.0
        })
    )
