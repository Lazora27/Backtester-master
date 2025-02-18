import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
