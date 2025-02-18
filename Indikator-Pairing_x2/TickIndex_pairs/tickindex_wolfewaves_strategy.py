import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
