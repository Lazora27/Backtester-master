import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'FisherSignals': 1.0
        })
    )
