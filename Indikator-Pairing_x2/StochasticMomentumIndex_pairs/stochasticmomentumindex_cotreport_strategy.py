import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und COTReport
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'COTReport': 1.0
        })
    )
