import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
