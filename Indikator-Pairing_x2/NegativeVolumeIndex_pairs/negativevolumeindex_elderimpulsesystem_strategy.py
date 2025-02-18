import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
