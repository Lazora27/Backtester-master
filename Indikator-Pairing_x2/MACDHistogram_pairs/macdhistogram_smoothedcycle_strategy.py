import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SmoothedCycle': 1.0
        })
    )
