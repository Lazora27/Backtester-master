import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'TimeCycle': 1.0
        })
    )
