import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'WolfeWaves': 1.0
        })
    )
