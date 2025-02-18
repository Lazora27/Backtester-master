import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
