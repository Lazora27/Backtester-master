import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
