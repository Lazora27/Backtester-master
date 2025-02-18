import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
