import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
