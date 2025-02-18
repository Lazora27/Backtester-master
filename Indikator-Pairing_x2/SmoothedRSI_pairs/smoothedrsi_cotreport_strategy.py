import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und COTReport
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'COTReport': 1.0
        })
    )
