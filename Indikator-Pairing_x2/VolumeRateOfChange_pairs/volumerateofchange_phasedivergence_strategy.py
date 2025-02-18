import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'PhaseDivergence': 1.0
        })
    )
