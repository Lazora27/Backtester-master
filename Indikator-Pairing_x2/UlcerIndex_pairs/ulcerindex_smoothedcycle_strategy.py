import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
