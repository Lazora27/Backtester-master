import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinAccumulationIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinAccumulationIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ChaikinAccumulationIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
