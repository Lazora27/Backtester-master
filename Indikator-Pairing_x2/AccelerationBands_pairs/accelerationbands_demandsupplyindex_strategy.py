import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
