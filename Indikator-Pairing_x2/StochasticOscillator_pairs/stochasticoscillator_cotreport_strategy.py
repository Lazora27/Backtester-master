import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und COTReport
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'COTReport': 1.0
        })
    )
