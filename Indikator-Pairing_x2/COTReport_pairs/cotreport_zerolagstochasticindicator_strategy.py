import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
