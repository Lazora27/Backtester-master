import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
