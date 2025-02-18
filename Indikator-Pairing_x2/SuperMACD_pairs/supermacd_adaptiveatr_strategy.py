import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AdaptiveATR': 1.0
        })
    )
