import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
