import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und CycleFinder
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'CycleFinder': 1.0
        })
    )
