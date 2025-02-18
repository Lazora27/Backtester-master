import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
