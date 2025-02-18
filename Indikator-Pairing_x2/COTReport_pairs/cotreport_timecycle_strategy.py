import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und TimeCycle
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'TimeCycle': 1.0
        })
    )
