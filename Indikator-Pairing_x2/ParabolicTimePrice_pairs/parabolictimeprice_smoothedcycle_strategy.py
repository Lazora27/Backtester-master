import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'SmoothedCycle': 1.0
        })
    )
