import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CCITurbo': 1.0
        })
    )
