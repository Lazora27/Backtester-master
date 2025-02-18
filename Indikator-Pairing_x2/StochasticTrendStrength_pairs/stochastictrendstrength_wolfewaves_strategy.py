import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WolfeWaves': 1.0
        })
    )
