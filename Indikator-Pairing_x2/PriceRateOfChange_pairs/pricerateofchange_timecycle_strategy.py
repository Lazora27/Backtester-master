import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'TimeCycle': 1.0
        })
    )
