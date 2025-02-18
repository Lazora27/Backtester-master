import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
