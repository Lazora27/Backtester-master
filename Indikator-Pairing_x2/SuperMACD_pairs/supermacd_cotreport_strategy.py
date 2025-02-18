import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und COTReport
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'COTReport': 1.0
        })
    )
