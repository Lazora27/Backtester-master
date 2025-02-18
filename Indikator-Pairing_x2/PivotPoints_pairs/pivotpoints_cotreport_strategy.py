import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und COTReport
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'COTReport': 1.0
        })
    )
