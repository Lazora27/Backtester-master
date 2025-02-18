import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
