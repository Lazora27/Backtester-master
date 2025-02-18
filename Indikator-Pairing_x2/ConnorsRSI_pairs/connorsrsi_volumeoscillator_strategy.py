import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'VolumeOscillator': 1.0
        })
    )
