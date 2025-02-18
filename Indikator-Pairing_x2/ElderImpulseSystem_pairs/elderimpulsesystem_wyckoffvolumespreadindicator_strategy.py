import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WyckoffVolumeSpreadIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WyckoffVolumeSpreadIndicator
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WyckoffVolumeSpreadIndicator': {
                'class': WyckoffVolumeSpreadIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffVolumeSpreadIndicator'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WyckoffVolumeSpreadIndicator': 1.0
        })
    )
