import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
