import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und COTReport
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'COTReport': 1.0
        })
    )
