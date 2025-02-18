import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'SeasonalStrength': 1.0
        })
    )
