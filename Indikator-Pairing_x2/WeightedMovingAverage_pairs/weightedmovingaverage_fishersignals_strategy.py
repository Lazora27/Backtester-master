import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und FisherSignals
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'FisherSignals': 1.0
        })
    )
