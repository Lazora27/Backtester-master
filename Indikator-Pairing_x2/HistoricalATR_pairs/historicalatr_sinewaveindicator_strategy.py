import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
