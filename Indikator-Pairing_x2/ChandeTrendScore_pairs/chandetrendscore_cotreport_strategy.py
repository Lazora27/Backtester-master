import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und COTReport
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'COTReport': 1.0
        })
    )
