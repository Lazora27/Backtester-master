import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
