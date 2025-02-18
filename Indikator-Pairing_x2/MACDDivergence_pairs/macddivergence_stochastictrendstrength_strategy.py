import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
