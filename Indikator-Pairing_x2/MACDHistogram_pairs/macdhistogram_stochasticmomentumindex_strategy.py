import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
