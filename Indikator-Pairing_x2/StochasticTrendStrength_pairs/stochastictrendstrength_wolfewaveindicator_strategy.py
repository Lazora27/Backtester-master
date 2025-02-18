import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
