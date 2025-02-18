import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AdaptiveATR': 1.0
        })
    )
