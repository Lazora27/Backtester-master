import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'IchimokuCloud': 1.0
        })
    )
