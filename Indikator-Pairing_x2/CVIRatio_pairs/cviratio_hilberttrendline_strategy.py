import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HilbertTrendline': 1.0
        })
    )
