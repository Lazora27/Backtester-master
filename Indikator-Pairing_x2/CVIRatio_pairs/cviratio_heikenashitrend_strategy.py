import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
