import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'WolfeWaves': 1.0
        })
    )
