import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
