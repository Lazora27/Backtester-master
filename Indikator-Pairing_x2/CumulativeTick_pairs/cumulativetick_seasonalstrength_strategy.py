import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SeasonalStrength': 1.0
        })
    )
