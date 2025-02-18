import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
