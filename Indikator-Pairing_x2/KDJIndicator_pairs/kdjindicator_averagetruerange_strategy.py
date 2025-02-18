import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
