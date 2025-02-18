import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
