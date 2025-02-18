import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'AverageLogRange': 1.0
        })
    )
