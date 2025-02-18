import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
