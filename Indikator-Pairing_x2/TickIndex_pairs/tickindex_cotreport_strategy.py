import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'COTReport': 1.0
        })
    )
