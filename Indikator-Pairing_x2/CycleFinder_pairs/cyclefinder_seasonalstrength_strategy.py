import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'SeasonalStrength': 1.0
        })
    )
