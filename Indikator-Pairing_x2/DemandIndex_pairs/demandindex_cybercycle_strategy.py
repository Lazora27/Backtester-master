import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
