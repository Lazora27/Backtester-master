import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
