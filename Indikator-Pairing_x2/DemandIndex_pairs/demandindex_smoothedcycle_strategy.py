import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
