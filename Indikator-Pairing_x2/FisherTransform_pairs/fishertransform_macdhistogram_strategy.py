import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MACDHistogram': 1.0
        })
    )
