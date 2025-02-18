import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
