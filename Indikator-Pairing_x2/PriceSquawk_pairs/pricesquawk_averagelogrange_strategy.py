import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AverageLogRange': 1.0
        })
    )
