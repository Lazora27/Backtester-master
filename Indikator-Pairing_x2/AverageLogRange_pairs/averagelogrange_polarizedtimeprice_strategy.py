import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
