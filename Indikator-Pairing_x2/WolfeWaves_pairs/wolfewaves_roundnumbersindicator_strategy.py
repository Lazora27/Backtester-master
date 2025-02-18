import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
