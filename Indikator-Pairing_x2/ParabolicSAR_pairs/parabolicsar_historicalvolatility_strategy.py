import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
