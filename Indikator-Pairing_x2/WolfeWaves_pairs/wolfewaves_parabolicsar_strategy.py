import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ParabolicSAR': 1.0
        })
    )
