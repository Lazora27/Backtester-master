import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
