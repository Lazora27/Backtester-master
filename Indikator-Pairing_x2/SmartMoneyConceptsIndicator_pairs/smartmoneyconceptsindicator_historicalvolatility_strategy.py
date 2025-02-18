import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartMoneyConceptsIndicator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartMoneyConceptsIndicator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SmartMoneyConceptsIndicator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
