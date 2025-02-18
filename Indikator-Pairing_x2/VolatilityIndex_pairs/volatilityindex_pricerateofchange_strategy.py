import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
