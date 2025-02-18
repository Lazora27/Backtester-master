import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
