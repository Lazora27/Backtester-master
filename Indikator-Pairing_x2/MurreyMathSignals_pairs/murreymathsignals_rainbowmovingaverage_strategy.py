import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
