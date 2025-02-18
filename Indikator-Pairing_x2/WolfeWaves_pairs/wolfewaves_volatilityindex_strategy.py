import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VolatilityIndex': 1.0
        })
    )
