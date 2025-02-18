import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'VolumeOscillator': 1.0
        })
    )
