import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
