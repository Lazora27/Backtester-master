import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'BradleySiderograph': 1.0
        })
    )
