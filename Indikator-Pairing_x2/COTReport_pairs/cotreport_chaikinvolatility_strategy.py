import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
