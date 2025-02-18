import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
