import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
