import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
