import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FisherSignals': 1.0
        })
    )
