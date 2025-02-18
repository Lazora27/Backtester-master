import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und COTReport
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'COTReport': 1.0
        })
    )
