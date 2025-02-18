import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'VolumeOscillator': 1.0
        })
    )
