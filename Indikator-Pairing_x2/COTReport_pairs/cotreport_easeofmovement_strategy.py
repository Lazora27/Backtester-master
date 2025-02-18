import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'EaseOfMovement': 1.0
        })
    )
