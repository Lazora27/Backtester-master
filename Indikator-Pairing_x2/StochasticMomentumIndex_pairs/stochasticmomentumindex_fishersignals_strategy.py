import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
