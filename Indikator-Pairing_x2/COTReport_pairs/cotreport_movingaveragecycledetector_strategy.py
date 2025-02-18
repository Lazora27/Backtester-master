import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
