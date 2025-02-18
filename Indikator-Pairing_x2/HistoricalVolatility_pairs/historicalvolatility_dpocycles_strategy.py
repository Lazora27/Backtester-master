import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'DPOCycles': 1.0
        })
    )
