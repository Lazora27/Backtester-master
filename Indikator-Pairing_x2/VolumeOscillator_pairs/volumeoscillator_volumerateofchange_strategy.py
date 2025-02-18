import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
