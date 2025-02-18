import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SeasonalStrength': 1.0
        })
    )
