import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
