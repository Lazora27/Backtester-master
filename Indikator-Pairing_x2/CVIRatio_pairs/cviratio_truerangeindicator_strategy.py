import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
