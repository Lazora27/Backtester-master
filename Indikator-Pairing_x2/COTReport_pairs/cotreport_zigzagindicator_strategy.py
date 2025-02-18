import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
