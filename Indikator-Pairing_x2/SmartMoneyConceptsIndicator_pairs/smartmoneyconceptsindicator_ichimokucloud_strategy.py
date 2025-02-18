import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartMoneyConceptsIndicator_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartMoneyConceptsIndicator und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'SmartMoneyConceptsIndicator': 1.0,
            'IchimokuCloud': 1.0
        })
    )
