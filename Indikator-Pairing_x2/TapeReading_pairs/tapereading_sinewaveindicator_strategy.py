import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
