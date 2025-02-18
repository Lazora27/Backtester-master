import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
