import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
