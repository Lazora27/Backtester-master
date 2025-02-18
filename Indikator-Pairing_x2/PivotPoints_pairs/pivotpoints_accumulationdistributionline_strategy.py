import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
