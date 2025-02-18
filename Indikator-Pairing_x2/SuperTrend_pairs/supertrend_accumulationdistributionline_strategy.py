import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
