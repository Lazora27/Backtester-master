import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'COTReport': 1.0
        })
    )
