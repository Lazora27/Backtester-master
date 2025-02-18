import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'SeasonalStrength': 1.0
        })
    )
