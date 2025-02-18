import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'COTReport': 1.0
        })
    )
