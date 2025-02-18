import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
