import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
