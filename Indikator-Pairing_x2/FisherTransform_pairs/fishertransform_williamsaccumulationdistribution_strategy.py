import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WilliamsAccumulationDistribution_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WilliamsAccumulationDistribution
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WilliamsAccumulationDistribution': 1.0
        })
    )
