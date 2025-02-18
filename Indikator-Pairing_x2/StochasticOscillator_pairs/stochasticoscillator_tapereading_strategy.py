import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
