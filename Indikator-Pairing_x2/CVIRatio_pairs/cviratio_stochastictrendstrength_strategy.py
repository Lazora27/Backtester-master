import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
