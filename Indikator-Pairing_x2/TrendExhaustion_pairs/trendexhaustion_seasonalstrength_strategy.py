import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SeasonalStrength': 1.0
        })
    )
