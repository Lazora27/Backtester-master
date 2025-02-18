import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedCycle_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedCycle und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SmoothedCycle': 1.0,
            'TimeCycle': 1.0
        })
    )
