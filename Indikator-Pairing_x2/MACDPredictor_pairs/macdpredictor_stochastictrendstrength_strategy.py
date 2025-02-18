import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
