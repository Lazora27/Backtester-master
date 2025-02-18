import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
