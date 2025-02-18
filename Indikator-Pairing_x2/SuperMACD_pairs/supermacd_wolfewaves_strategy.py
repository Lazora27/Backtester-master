import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WolfeWaves': 1.0
        })
    )
