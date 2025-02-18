import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und MassIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'MassIndex': 1.0
        })
    )
