import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
