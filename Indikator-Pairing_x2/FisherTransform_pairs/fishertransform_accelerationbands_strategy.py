import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AccelerationBands': 1.0
        })
    )
