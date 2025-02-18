import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
