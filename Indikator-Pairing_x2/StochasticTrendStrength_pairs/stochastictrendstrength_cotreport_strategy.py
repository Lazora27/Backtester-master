import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und COTReport
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'COTReport': 1.0
        })
    )
