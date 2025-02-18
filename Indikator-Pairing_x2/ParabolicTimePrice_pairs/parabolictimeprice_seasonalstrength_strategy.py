import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'SeasonalStrength': 1.0
        })
    )
