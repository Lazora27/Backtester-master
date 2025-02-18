import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
