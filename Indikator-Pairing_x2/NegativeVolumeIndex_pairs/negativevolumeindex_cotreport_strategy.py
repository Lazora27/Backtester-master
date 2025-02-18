import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'COTReport': 1.0
        })
    )
