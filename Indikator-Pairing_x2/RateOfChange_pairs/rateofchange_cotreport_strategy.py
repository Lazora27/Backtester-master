import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und COTReport
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'COTReport': 1.0
        })
    )
