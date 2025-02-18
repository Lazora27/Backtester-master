import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'UltimateOscillator': 1.0
        })
    )
