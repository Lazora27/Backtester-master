import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AdaptiveATR': 1.0
        })
    )
