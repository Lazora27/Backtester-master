import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und OpenInterest
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'OpenInterest': 1.0
        })
    )
