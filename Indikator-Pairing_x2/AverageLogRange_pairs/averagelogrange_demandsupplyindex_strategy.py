import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
