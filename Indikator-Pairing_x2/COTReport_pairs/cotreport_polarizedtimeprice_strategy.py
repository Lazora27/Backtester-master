import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
