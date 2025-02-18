import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
