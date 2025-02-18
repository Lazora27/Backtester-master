import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
