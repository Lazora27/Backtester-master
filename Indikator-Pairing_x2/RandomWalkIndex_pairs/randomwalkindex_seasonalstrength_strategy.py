import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
