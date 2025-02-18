import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'SeasonalStrength': 1.0
        })
    )
