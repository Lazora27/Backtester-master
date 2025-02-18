import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
