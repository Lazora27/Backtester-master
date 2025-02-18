import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
