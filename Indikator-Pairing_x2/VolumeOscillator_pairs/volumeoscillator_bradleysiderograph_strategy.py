import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'BradleySiderograph': 1.0
        })
    )
