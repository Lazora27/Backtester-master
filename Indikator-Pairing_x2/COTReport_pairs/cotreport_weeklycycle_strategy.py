import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'WeeklyCycle': 1.0
        })
    )
