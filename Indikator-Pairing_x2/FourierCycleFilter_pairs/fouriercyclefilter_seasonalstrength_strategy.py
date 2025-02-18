import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'SeasonalStrength': 1.0
        })
    )
