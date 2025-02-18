import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
