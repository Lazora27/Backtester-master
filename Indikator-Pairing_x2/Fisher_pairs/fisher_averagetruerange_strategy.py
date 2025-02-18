import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AverageTrueRange': 1.0
        })
    )
