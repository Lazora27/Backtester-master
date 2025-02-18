import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
