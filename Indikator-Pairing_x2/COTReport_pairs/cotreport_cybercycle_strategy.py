import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und CyberCycle
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'CyberCycle': 1.0
        })
    )
