import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HullMovingAverage': 1.0
        })
    )
