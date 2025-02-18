import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
