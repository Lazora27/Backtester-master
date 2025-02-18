import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
