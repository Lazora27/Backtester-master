import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
