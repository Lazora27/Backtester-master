import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
