import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'StochasticRSI': 1.0
        })
    )
