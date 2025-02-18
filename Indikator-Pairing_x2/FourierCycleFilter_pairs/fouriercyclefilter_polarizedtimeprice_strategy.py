import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
