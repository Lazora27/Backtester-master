import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AutoFibonacci': 1.0
        })
    )
