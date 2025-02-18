import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
