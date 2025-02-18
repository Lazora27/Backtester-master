import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
