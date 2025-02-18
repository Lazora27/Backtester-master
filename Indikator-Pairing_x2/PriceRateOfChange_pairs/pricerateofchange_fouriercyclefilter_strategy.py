import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
