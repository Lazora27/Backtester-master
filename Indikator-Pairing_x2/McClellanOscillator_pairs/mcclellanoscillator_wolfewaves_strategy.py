import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
