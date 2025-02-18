import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und COTReport
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'COTReport': 1.0
        })
    )
