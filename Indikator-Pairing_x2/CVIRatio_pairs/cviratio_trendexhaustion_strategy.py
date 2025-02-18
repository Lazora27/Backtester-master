import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TrendExhaustion': 1.0
        })
    )
