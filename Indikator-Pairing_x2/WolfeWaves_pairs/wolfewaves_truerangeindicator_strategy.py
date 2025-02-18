import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
