import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
