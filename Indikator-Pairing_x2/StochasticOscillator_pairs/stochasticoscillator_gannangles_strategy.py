import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und GannAngles
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'GannAngles': 1.0
        })
    )
