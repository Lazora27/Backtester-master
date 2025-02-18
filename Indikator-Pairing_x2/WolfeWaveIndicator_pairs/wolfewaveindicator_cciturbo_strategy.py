import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
