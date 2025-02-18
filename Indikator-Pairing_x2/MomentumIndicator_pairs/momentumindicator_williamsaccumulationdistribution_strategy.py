import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_WilliamsAccumulationDistribution_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und WilliamsAccumulationDistribution
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'WilliamsAccumulationDistribution': 1.0
        })
    )
