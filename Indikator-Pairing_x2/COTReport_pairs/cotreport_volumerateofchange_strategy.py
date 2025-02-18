import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
