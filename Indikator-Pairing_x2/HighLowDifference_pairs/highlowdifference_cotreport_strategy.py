import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und COTReport
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'COTReport': 1.0
        })
    )
