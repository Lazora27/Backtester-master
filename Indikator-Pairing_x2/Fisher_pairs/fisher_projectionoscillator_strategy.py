import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
