import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
