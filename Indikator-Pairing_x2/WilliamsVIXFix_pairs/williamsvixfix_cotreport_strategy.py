import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und COTReport
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'COTReport': 1.0
        })
    )
