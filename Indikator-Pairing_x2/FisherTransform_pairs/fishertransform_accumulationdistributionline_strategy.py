import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
