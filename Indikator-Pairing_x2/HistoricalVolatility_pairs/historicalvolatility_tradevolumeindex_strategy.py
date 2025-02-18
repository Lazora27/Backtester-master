import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
