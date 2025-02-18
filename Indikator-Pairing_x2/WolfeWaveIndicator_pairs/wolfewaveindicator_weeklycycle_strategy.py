import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
