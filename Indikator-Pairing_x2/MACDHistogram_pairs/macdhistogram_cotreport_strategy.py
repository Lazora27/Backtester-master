import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und COTReport
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'COTReport': 1.0
        })
    )
