import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
