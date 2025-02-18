import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
