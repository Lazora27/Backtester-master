import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und OpenInterest
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'OpenInterest': 1.0
        })
    )
