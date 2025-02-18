import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
