import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FisherSignals': 1.0
        })
    )
