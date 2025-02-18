import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'COTReport': 1.0
        })
    )
