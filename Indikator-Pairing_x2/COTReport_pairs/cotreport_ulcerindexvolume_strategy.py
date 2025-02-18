import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
