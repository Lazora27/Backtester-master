import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'VWAPBands': 1.0
        })
    )
