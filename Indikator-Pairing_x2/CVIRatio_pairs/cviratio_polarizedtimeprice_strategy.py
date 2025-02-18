import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
