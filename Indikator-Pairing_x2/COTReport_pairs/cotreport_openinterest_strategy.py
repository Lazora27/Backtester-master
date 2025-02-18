import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und OpenInterest
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'OpenInterest': 1.0
        })
    )
