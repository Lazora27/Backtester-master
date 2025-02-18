import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SeasonalStrength': 1.0
        })
    )
