import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
