import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'VolumeOscillator': 1.0
        })
    )
