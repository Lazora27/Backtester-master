import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
