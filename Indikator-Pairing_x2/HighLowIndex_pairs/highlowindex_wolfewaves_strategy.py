import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
