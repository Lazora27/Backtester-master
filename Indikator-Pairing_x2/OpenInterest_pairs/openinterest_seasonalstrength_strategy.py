import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'SeasonalStrength': 1.0
        })
    )
