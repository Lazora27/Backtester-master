import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und COTReport
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'COTReport': 1.0
        })
    )
