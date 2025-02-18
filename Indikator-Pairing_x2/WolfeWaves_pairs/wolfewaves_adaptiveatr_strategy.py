import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AdaptiveATR': 1.0
        })
    )
