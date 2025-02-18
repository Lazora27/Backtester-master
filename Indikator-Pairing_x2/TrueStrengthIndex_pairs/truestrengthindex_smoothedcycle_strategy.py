import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
