import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
