import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
