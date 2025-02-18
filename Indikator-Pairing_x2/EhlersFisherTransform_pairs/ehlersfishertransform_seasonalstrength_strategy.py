import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'SeasonalStrength': 1.0
        })
    )
