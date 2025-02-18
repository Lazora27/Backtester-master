import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'VolumeOscillator': 1.0
        })
    )
