import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
