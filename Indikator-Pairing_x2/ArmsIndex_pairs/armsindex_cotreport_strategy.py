import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'COTReport': 1.0
        })
    )
