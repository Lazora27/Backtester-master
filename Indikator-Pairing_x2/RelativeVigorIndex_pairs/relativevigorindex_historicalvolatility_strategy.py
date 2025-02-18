import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
