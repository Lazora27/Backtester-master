import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
