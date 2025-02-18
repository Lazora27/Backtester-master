import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'VolumeOscillator': 1.0
        })
    )
