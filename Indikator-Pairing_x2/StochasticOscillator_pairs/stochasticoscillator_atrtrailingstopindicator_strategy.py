import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ATRTrailingStopIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ATRTrailingStopIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ATRTrailingStopIndicator': 1.0
        })
    )
