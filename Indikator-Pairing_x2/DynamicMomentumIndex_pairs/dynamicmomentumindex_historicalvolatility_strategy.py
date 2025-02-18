import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
