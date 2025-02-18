import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
