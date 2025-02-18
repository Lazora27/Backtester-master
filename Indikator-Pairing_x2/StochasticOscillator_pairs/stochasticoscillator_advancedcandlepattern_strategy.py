import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
