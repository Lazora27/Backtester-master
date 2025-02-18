import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
