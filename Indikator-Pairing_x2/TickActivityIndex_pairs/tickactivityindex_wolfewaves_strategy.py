import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
