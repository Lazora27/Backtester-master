import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TrueRange': 1.0
        })
    )
