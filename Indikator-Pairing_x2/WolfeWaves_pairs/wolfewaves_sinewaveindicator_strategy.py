import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
