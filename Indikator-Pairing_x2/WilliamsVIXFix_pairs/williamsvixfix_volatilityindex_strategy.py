import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'VolatilityIndex': 1.0
        })
    )
