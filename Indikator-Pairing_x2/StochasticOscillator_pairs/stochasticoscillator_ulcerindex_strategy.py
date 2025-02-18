import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'UlcerIndex': 1.0
        })
    )
