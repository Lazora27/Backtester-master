import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und COTReport
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'COTReport': 1.0
        })
    )
