import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
