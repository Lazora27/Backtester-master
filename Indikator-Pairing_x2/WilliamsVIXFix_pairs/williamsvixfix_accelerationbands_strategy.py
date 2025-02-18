import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AccelerationBands': 1.0
        })
    )
