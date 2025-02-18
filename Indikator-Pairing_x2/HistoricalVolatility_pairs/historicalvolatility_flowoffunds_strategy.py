import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'FlowOfFunds': 1.0
        })
    )
