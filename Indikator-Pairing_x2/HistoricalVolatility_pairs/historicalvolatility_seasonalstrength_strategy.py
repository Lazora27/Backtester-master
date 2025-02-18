import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'SeasonalStrength': 1.0
        })
    )
