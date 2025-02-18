import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'SmoothedCycle': 1.0
        })
    )
