import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
