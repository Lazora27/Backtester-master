import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
