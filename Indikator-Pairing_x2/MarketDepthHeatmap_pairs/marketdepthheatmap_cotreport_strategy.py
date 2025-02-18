import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und COTReport
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'COTReport': 1.0
        })
    )
