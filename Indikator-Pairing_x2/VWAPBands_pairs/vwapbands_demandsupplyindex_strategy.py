import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
