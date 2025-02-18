import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SeasonalStrength': 1.0
        })
    )
