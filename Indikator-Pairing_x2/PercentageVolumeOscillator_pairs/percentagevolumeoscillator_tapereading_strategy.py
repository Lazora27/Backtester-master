import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentageVolumeOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentageVolumeOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'PercentageVolumeOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
