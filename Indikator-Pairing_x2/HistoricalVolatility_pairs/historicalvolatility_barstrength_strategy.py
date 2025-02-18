import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und BarStrength
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'BarStrength': 1.0
        })
    )
