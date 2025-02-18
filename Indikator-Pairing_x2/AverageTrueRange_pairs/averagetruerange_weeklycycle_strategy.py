import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'WeeklyCycle': 1.0
        })
    )
