import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'StochasticRSI': 1.0
        })
    )
