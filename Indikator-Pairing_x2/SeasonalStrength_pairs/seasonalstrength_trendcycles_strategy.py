import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'TrendCycles': 1.0
        })
    )
