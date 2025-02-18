import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und COTReport
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'COTReport': 1.0
        })
    )
