import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AccelerationBands': 1.0
        })
    )
