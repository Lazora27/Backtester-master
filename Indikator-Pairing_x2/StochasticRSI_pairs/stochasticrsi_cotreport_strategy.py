import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und COTReport
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'COTReport': 1.0
        })
    )
