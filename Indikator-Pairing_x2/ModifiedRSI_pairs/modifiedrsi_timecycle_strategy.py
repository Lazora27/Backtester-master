import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TimeCycle': 1.0
        })
    )
