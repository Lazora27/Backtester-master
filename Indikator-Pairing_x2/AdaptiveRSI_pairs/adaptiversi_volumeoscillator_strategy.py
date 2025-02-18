import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'VolumeOscillator': 1.0
        })
    )
