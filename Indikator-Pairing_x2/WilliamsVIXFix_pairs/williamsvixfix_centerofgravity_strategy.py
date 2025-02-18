import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'CenterOfGravity': 1.0
        })
    )
