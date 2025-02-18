import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und COTReport
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'COTReport': 1.0
        })
    )
