import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
