import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und COTReport
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'COTReport': 1.0
        })
    )
