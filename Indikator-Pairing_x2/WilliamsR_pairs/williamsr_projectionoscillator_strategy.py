import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
