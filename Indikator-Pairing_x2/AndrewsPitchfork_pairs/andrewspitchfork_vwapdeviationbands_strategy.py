import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
