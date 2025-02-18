import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
