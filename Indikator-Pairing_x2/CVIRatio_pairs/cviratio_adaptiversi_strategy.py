import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
