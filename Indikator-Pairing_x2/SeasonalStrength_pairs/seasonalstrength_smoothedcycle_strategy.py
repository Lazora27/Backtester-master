import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'SmoothedCycle': 1.0
        })
    )
