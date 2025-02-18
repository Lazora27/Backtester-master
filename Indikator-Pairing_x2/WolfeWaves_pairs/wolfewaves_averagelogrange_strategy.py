import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AverageLogRange': 1.0
        })
    )
