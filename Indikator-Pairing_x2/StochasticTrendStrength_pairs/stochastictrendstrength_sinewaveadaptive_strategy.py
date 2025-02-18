import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
