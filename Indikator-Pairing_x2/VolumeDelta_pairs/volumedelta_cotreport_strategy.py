import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und COTReport
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'COTReport': 1.0
        })
    )
