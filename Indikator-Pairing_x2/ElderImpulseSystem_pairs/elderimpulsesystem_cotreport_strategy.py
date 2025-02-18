import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und COTReport
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'COTReport': 1.0
        })
    )
