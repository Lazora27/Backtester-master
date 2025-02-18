import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
