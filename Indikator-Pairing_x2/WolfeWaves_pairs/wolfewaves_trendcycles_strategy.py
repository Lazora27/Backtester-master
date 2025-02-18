import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und TrendCycles
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'TrendCycles': 1.0
        })
    )
