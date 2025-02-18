import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'SmoothedCycle': 1.0
        })
    )
