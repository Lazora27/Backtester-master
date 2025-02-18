import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArnaudLegouxMovingAverage_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArnaudLegouxMovingAverage und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ArnaudLegouxMovingAverage': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
