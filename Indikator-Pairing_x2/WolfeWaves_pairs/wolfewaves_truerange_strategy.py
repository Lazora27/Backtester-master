import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TrueRange
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TrueRange': 1.0
        })
    )
