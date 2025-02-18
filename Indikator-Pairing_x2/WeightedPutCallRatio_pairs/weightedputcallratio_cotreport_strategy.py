import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und COTReport
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'COTReport': 1.0
        })
    )
