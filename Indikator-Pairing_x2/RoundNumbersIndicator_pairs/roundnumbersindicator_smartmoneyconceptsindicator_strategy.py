import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_SmartMoneyConceptsIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und SmartMoneyConceptsIndicator
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'SmartMoneyConceptsIndicator': 1.0
        })
    )
