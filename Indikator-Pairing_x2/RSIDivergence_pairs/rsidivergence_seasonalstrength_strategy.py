import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SeasonalStrength': 1.0
        })
    )
