import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'SeasonalStrength': 1.0
        })
    )
