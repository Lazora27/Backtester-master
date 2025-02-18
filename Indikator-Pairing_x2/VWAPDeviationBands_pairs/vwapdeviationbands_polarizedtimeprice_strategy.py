import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
