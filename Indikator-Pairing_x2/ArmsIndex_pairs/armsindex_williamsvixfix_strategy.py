import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
