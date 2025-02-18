import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'VolumeOscillator': 1.0
        })
    )
