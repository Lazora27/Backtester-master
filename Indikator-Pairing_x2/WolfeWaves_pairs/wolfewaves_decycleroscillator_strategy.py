import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
