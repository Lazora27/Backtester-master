import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'FearGreedIndex': 1.0
        })
    )
