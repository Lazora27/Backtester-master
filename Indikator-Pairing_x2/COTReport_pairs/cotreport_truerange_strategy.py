import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TrueRange
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TrueRange': 1.0
        })
    )
