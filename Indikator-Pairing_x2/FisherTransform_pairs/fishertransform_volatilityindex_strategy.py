import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VolatilityIndex': 1.0
        })
    )
