import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
