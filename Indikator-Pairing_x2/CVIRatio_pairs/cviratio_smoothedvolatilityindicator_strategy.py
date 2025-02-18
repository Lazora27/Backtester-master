import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SmoothedVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SmoothedVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SmoothedVolatilityIndicator': 1.0
        })
    )
