import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SuperMACD': 1.0
        })
    )
