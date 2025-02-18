import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'SmoothedCycle': 1.0
        })
    )
