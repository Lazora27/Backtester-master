import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
