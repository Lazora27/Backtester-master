import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
