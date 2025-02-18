import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und COTReport
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'COTReport': 1.0
        })
    )
