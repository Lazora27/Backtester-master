import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und COTReport
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'COTReport': 1.0
        })
    )
