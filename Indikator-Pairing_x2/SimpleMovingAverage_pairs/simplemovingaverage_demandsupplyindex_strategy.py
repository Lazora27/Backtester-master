import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
