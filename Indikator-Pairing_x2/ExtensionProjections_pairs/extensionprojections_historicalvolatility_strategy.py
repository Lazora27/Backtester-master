import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
