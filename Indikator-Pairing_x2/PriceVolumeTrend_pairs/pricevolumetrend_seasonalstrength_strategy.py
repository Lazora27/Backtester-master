import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'SeasonalStrength': 1.0
        })
    )
