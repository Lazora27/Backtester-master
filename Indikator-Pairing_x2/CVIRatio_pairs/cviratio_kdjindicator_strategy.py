import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'KDJIndicator': 1.0
        })
    )
