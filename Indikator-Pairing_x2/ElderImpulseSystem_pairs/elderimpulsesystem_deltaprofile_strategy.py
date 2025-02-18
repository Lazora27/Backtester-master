import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'DeltaProfile': 1.0
        })
    )
