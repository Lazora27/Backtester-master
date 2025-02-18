import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
