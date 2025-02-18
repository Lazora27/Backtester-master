import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WilliamsR
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WilliamsR': 1.0
        })
    )
