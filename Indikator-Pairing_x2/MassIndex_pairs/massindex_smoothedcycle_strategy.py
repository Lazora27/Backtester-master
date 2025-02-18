import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
