import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
