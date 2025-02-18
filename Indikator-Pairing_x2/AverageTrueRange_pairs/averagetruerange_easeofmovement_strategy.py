import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'EaseOfMovement': 1.0
        })
    )
