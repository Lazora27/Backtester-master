import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und COTReport
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'COTReport': 1.0
        })
    )
