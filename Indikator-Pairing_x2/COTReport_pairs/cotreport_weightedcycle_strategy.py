import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'WeightedCycle': 1.0
        })
    )
