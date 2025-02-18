import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'WolfeWaves': 1.0
        })
    )
