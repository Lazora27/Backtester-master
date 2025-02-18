import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AdaptiveATR': 1.0
        })
    )
