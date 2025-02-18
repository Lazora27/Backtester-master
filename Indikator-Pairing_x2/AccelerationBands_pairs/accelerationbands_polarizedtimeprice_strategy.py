import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
