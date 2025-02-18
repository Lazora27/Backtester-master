import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsAccumulationDistribution_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsAccumulationDistribution und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'WilliamsAccumulationDistribution': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
