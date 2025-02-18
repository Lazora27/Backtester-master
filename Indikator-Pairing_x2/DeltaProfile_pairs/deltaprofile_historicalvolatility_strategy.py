import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
