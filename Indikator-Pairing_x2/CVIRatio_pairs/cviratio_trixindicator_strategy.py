import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TRIXIndicator': 1.0
        })
    )
