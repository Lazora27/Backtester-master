import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SeasonalStrength': 1.0
        })
    )
