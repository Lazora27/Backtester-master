import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'WeightedCycle': 1.0
        })
    )
