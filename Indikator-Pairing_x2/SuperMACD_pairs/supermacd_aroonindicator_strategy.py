import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AroonIndicator': 1.0
        })
    )
