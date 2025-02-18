import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
