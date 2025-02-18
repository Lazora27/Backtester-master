import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
