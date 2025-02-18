import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und COTReport
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'COTReport': 1.0
        })
    )
