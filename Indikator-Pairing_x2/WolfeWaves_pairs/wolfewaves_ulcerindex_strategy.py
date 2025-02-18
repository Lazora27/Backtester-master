import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'UlcerIndex': 1.0
        })
    )
