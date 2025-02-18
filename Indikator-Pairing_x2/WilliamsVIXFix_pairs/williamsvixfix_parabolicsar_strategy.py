import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ParabolicSAR': 1.0
        })
    )
