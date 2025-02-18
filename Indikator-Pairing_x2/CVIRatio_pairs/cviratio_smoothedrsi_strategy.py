import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SmoothedRSI': 1.0
        })
    )
