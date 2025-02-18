import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_ArmsEaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und ArmsEaseOfMovement
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'ArmsEaseOfMovement': 1.0
        })
    )
