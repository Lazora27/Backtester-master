import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SuperTrend
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SuperTrend': 1.0
        })
    )
