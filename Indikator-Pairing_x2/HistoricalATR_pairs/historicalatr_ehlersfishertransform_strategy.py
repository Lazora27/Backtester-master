import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
