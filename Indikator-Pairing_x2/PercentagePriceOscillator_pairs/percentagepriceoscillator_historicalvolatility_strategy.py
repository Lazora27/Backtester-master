import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
