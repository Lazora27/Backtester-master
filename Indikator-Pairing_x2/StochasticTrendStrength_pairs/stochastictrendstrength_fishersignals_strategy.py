import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FisherSignals': 1.0
        })
    )
