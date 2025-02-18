import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'SeasonalStrength': 1.0
        })
    )
