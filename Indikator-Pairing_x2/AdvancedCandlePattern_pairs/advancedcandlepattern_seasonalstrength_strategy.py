import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'SeasonalStrength': 1.0
        })
    )
