import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
