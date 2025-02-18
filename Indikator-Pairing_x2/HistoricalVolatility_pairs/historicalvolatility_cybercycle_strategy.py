import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und CyberCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'CyberCycle': 1.0
        })
    )
