import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
