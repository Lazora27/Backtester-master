import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
