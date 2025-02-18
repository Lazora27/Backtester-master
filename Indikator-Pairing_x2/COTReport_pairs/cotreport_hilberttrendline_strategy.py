import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HilbertTrendline': 1.0
        })
    )
