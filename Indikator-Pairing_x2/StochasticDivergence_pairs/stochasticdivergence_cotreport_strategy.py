import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und COTReport
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'COTReport': 1.0
        })
    )
