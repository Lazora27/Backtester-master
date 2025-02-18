import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'VortexIndicator': 1.0
        })
    )
