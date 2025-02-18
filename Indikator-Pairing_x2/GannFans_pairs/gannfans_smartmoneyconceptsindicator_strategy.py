import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SmartMoneyConceptsIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SmartMoneyConceptsIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SmartMoneyConceptsIndicator': 1.0
        })
    )
