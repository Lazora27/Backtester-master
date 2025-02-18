import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
