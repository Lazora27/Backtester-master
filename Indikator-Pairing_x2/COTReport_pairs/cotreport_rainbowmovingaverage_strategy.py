import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
