import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'COTReport': 1.0
        })
    )
