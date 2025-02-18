import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und COTReport
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'COTReport': 1.0
        })
    )
