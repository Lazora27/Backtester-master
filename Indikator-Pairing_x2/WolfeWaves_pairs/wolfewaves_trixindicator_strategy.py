import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TRIXIndicator': 1.0
        })
    )
