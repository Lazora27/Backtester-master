import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AverageLogRange': 1.0
        })
    )
