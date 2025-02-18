import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
