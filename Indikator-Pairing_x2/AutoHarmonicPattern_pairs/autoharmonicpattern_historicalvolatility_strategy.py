import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
