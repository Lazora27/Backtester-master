import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AutoFibonacci': 1.0
        })
    )
