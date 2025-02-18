import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MACDHistogram': 1.0
        })
    )
