import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
