import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
