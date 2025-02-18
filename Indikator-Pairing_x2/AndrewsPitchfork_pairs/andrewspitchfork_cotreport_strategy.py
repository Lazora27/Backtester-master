import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und COTReport
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'COTReport': 1.0
        })
    )
