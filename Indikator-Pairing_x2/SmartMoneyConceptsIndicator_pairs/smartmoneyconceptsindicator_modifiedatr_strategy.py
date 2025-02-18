import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartMoneyConceptsIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartMoneyConceptsIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SmartMoneyConceptsIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
