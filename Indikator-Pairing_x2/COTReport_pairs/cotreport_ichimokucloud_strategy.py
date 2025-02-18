import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'IchimokuCloud': 1.0
        })
    )
