import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und COTReport
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'COTReport': 1.0
        })
    )
