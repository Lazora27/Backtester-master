import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'CenterOfGravity': 1.0
        })
    )
