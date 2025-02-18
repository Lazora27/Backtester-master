import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
