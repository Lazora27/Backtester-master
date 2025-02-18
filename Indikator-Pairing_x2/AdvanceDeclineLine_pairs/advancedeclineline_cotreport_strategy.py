import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und COTReport
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'COTReport': 1.0
        })
    )
