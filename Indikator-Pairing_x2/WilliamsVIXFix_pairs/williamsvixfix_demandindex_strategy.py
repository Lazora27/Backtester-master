import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DemandIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DemandIndex': 1.0
        })
    )
