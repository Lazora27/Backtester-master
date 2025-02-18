import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
