import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
