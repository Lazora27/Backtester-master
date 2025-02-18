import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'SmoothedCycle': 1.0
        })
    )
