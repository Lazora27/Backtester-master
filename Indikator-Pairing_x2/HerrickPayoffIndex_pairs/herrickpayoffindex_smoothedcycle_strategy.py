import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
