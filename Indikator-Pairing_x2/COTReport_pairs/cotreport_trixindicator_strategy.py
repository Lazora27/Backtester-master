import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TRIXIndicator': 1.0
        })
    )
