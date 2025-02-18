import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VolumeOscillator': 1.0
        })
    )
