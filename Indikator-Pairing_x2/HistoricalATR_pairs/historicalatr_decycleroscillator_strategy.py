import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
