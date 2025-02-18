import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'COTReport': 1.0
        })
    )
