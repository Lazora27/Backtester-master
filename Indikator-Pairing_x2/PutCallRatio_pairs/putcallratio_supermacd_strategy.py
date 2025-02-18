import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SuperMACD
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SuperMACD': 1.0
        })
    )
