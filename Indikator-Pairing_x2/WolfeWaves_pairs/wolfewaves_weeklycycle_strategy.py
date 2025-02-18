import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'WeeklyCycle': 1.0
        })
    )
