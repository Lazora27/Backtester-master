import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
