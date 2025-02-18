import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
