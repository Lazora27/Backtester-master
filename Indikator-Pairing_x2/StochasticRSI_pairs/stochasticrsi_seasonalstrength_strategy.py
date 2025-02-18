import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SeasonalStrength': 1.0
        })
    )
