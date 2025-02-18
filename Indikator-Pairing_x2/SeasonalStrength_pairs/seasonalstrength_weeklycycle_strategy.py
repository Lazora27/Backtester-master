import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'WeeklyCycle': 1.0
        })
    )
