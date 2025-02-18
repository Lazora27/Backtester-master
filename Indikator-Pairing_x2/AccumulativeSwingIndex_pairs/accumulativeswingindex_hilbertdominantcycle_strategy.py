import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulativeSwingIndex_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulativeSwingIndex und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AccumulativeSwingIndex': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
