import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HistoricalATR': 1.0
        })
    )
